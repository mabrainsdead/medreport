# Generated by Django 2.2.1 on 2019-06-20 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrApp', '0003_auto_20190602_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='conduta',
        ),
    ]
