# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('info_second_name', models.CharField(max_length=50, help_text='Резервное поле для отображения')),
                ('info_maplink', models.TextField(help_text='Ссылка на карту')),
                ('info_price', models.TextField(help_text='Расценки')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=40, help_text='Название арендуемого места')),
                ('place_adress', models.TextField(help_text='Адрес места')),
                ('place_area', models.TextField(help_text='Рамки по площади')),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='place_id',
            field=models.ForeignKey(to='Arenda.Place'),
        ),
    ]
