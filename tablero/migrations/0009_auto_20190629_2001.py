# Generated by Django 2.2.2 on 2019-06-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0001_initial'),
        ('tablero', '0008_auto_20190629_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kpi_tablero',
            name='indicador',
        ),
        migrations.AddField(
            model_name='tablero',
            name='indicador',
            field=models.ManyToManyField(blank=True, to='indicador.Indicador'),
        ),
    ]
