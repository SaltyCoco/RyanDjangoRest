# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-17 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('hour', models.IntegerField()),
                ('cntFormer', models.IntegerField()),
                ('sumFormer', models.CharField(default='', max_length=15)),
                ('cntNewDM', models.IntegerField()),
                ('sumNewDM', models.CharField(default='', max_length=15)),
                ('cntNew', models.IntegerField()),
                ('sumNew', models.CharField(default='', max_length=15)),
                ('cntITA', models.IntegerField()),
                ('sumITA', models.CharField(default='', max_length=15)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='cdl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('hour', models.IntegerField()),
                ('denialReason', models.CharField(default='', max_length=100)),
                ('cntDenial', models.IntegerField()),
                ('sumDenials', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='cpb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('hour', models.IntegerField()),
                ('cntCR', models.IntegerField()),
                ('sumCR', models.CharField(default='', max_length=15)),
                ('cntCDP', models.IntegerField()),
                ('sumCDP', models.CharField(default='', max_length=15)),
                ('cntCDR', models.IntegerField()),
                ('sumCDR', models.CharField(default='', max_length=15)),
                ('cntCV', models.IntegerField()),
                ('sumCV', models.CharField(default='', max_length=15)),
                ('cntPA', models.IntegerField()),
                ('sumPA', models.CharField(default='', max_length=15)),
                ('cntPR', models.IntegerField()),
                ('sumPR', models.CharField(default='', max_length=15)),
                ('cntP', models.IntegerField()),
                ('sumP', models.CharField(default='', max_length=15)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='cpl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('hour', models.IntegerField()),
                ('cntFormer', models.IntegerField()),
                ('sumFormer', models.CharField(default='', max_length=15)),
                ('cntNewDM', models.IntegerField()),
                ('sumNewDM', models.CharField(default='', max_length=15)),
                ('cntNew', models.IntegerField()),
                ('sumNew', models.CharField(default='', max_length=15)),
                ('cntITA', models.IntegerField()),
                ('sumITA', models.CharField(default='', max_length=15)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
