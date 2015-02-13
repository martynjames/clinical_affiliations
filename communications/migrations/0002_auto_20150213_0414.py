# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communication',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='communication',
            name='datestamp',
            field=models.DateField(default=datetime.datetime(2015, 2, 13, 4, 14, 3, 882745, tzinfo=utc), verbose_name=b'communication date'),
            preserve_default=False,
        ),
    ]
