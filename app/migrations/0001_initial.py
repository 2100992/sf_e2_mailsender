# Generated by Django 3.0.2 on 2020-02-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailSender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_email', models.CharField(max_length=150)),
                ('mailtext', models.TextField()),
                ('time_to_send', models.BigIntegerField()),
            ],
        ),
    ]
