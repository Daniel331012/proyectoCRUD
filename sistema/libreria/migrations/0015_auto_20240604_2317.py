# Generated by Django 3.2.8 on 2024-06-05 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0014_auto_20240604_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabla9',
            old_name='Descripcion9',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='tabla9',
            old_name='N9',
            new_name='numero',
        ),
    ]
