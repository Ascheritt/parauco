# Generated by Django 2.2.2 on 2019-06-29 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0002_tablero_indicador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablero',
            name='indicador',
        ),
    ]
