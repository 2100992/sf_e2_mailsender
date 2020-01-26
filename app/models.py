from django.db import models

# Create your models here.

class MailSender(models.Model):
    rec_email = models.CharField(max_length=150)
    mailtext = models.TextField()
    time_to_send = models.DateTimeField()