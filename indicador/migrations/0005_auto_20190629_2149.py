# Generated by Django 2.2.2 on 2019-06-30 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0004_auto_20190629_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='indicador',
        ),
        migrations.AddField(
            model_name='indicador',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='indicador.Categoria'),
            preserve_default=False,
        ),
    ]
