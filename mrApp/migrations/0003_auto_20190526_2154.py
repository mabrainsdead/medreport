# Generated by Django 2.2.1 on 2019-05-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrApp', '0002_auto_20190526_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateTimeField(),
        ),
    ]
