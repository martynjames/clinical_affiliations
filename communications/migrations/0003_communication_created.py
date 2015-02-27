# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0002_auto_20150213_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 27, 4, 20, 31, 547580, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
