# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('height', models.FloatField(blank=True, default=None, null=True)),
                ('hash', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='KladMan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, default=None, max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='geotag',
            name='kladman',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kladmanweb.KladMan'),
        ),
    ]
