# Generated by Django 2.2.1 on 2019-05-18 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='name',
            new_name='nome',
        ),
    ]