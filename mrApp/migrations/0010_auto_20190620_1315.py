# Generated by Django 2.2.1 on 2019-06-20 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrApp', '0009_receituario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receituario',
            old_name='atendimento_id',
            new_name='atendimento',
        ),
        migrations.AddField(
            model_name='receituario',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mrApp.Paciente'),
        ),
    ]
