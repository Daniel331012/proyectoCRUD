# Generated by Django 3.2.8 on 2024-06-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0009_auto_20240516_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='tabla10',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Num', models.CharField(default=' ', max_length=100, verbose_name='N')),
                ('Desc', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.AlterField(
            model_name='tabla9',
            name='Descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tabla9',
            name='N',
            field=models.CharField(default=' ', max_length=100, verbose_name='N'),
        ),
    ]
