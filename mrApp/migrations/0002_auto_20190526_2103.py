# Generated by Django 2.2.1 on 2019-05-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
