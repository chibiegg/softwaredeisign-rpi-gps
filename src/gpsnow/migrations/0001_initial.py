# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transponder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='名前', max_length=20, unique=True)),
                ('description', models.CharField(verbose_name='説明', blank=True, max_length=100)),
                ('marker', models.ImageField(verbose_name='マーカー', blank=True, upload_to='uploads/markers')),
                ('marker_disabled', models.ImageField(verbose_name='マーカー (無効時)', blank=True, upload_to='uploads/markers')),
            ],
            options={
                'verbose_name': '発信機',
                'verbose_name_plural': '発信機',
            },
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='時刻')),
                ('latitude', models.DecimalField(verbose_name='緯度', null=True, blank=True, max_digits=10, decimal_places=5)),
                ('longitude', models.DecimalField(verbose_name='軽度', null=True, blank=True, max_digits=10, decimal_places=5)),
                ('transponder', models.ForeignKey(to='gpsnow.Transponder')),
            ],
            options={
                'verbose_name': '位置情報',
                'verbose_name_plural': '位置情報',
            },
        ),
    ]
