# Generated by Django 2.2.2 on 2019-07-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0016_auto_20190701_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='meta_kpi',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='info_kpi',
            name='valor_kpi',
            field=models.IntegerField(max_length=3),
        ),
    ]
