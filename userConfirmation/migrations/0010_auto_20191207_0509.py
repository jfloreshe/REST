# Generated by Django 2.2.7 on 2019-12-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userConfirmation', '0009_auto_20191207_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]