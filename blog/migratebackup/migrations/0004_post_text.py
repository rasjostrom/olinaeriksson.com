# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 6, 9, 3, 6, 44, 271891, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
