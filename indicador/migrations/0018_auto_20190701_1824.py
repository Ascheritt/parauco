# Generated by Django 2.1 on 2019-07-01 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0017_auto_20190701_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='meta_kpi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='info_kpi',
            name='valor_kpi',
            field=models.IntegerField(),
        ),
    ]
