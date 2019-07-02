# Generated by Django 2.2.2 on 2019-06-29 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0001_initial'),
        ('tablero', '0005_auto_20190629_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kpi_tablero',
            name='indicador',
        ),
        migrations.AddField(
            model_name='kpi_tablero',
            name='indicador',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='indicador.Indicador'),
            preserve_default=False,
        ),
    ]
