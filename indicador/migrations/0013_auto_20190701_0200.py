# Generated by Django 2.2.2 on 2019-07-01 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0012_auto_20190701_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_kpi',
            name='indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicador.Indicador'),
        ),
    ]
