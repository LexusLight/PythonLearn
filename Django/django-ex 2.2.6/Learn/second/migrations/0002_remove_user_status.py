# Generated by Django 2.2.6 on 2020-01-10 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
