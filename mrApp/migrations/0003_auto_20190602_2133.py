# Generated by Django 2.2.1 on 2019-06-02 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrApp', '0002_consulta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consulta',
            new_name='Atendimento',
        ),
        migrations.RenameField(
            model_name='atendimento',
            old_name='data',
            new_name='data_atendimento',
        ),
    ]
