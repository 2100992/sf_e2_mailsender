from django import forms

class MailForm(forms.Form):
    rec_email = forms.EmailField(label='recEmail')
    mailtext = forms.CharField(label='mailText')
    sending_delay = forms.IntegerField(label='sendingDelay')

