# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Smartelec', '0002_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='deviceStatus',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
