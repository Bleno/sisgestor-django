# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eixo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('curso', models.CharField(max_length=45)),
                ('sigla', models.CharField(max_length=3)),
                ('ativo', models.BooleanField(default=True)),
                ('id_eixo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eixo.Eixo')),
            ],
        ),
    ]
