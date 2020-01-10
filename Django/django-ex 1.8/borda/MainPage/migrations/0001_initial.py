# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('category_name', models.CharField(max_length=50, help_text='Имя категории')),
                ('category_info', models.TextField(help_text='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('thread_autor', models.CharField(max_length=30, help_text='Автор комментария')),
                ('comment_text', models.TextField(help_text='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('thread_autor', models.CharField(max_length=30, help_text='Автор треда')),
                ('thread_name', models.CharField(max_length=100, help_text='Имя треда')),
                ('thread_text', models.TextField(help_text='Текст внутри треда')),
                ('category_id', models.ForeignKey(to='MainPage.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='thread_id',
            field=models.ForeignKey(to='MainPage.Threads'),
        ),
    ]
