# Generated by Django 3.2.8 on 2024-05-16 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0007_rename_tablanueve_tabla9'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabla9',
            old_name='Descripcion',
            new_name='Descripcions',
        ),
    ]
