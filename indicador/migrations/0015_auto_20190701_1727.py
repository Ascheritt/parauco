# Generated by Django 2.2.2 on 2019-07-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0014_auto_20190701_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='meta_kpi',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='info_kpi',
            name='valor_kpi',
            field=models.IntegerField(max_length=10),
        ),
    ]
