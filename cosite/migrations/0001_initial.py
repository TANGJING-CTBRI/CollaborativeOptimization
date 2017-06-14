# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetectedParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.IntegerField(default=0, help_text='异常检测标签(-1,0,1)')),
                ('ave_anneal_soak_t', models.FloatField(help_text='连退均热温度平均值')),
                ('ave_anneal_rapid_cool_outlet_t', models.FloatField(help_text='连退快冷出口温度平均值')),
                ('ave_anneal_slow_cool_outlet_t', models.FloatField(help_text='连退缓冷出口温度平均值')),
                ('pc', models.FloatField(help_text='C%')),
                ('pmn', models.FloatField(help_text='Mn%')),
                ('pp', models.FloatField(help_text='P%')),
                ('ps', models.FloatField(help_text='S%')),
                ('finishing_inlet_t', models.FloatField(help_text='精轧入口温度')),
                ('finishing_outlet_t', models.FloatField(help_text='精轧出口温度')),
                ('coiling_t', models.FloatField(help_text='卷取温度')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间')),
            ],
        ),
    ]
