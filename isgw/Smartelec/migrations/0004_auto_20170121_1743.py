# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Smartelec', '0003_device_devicestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deviceStatus',
            field=models.CharField(default=b'false', max_length=10),
        ),
    ]
