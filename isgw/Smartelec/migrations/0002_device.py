# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Smartelec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceid', models.IntegerField(unique=True)),
                ('devicerating', models.CharField(default=b'0 W', max_length=255)),
                ('user', models.OneToOneField(to='Smartelec.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
