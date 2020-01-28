from django.contrib import admin
from .models import MailSender

# Register your models here.

@admin.register(MailSender)
class InfoMailSender(admin.ModelAdmin):
    pass
