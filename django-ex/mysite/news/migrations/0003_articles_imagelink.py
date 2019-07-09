# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190706_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='imagelink',
            field=models.CharField(max_length=50, default='glad'),
        ),
    ]
