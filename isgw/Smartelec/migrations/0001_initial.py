# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(default=0, unique=True)),
                ('month', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('predicted_low', models.IntegerField(default=0)),
                ('current_rate', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('creditUnits', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskId', models.IntegerField(default=0, unique=True)),
                ('taskHour', models.IntegerField(default=0)),
                ('taskMinutes', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to='Smartelec.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transactionid', models.IntegerField(default=0, unique=True)),
                ('transactionUnitAmount', models.IntegerField(default=0)),
                ('numberTransactionUnits', models.IntegerField(default=0)),
                ('transactionUserId', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to='Smartelec.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
