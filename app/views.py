from datetime import datetime
from django.shortcuts import render, redirect

from django.views import View
from django.views.generic.edit import FormView

from django.urls import reverse

# from django.forms import ModelForm
from .forms import MailForm
from .models import MailSender
from .utils import SenderThread

from datetime import datetime, timedelta, timezone


# Create your views here.

class Index(View):
    ''' Функционал вьюхи:
    - по get запросу показывает форму и очередь отправок
    - по post запросу поднимает новый поток с указанной задержкой отправки письма
        и пишет в базу информацю о это отправке
    '''

    template = 'app/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # Готовим данные для отображения очереди отправок
        # Последние 10 писем отсортированные по времени отрпвки
        # senders = MailSender.objects.all().order_by('time_to_send').reverse()[:10]
        senders = MailSender.objects.order_by('id').reverse().all()[:10]

        # Добавим в контекст поле об отправлено/не_отправлено
        # похорошему этот функционал нужно выносить на сторону JS
        # Но это потом
        for sender in senders:
            if sender.time_to_send < datetime.now(timezone.utc):
                setattr(sender, 'sent', False)
            else:
                setattr(sender, 'sent', True)

        context['mailsenders'] = senders

        return render(request, self.template, context=context)

    def post(self, request, *args, **kwargs):
        mail_form = MailForm(request.POST)
        if mail_form.is_valid():

            # Поднимаем новый тред на отправку письма
            sender_thread = SenderThread(**mail_form.cleaned_data)
            sender_thread.start()

            # Вычислим приблизительное время отправки письма
            time_to_send = datetime.now() + timedelta(seconds=mail_form.cleaned_data['sending_delay'])
            # Готовим оставшиеся данные для сохранения в базу
            mailtext = mail_form.cleaned_data.get('mailtext')
            rec_email = mail_form.cleaned_data.get('rec_email')

            sender_to_models = MailSender(rec_email=rec_email, mailtext=mailtext, time_to_send=time_to_send)
            sender_to_models.save()

        else:
            print(mail_form.errors)

        return redirect(reverse('index_url'))