# Generated by Django 3.0.2 on 2020-06-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('D', '0002_auto_20200626_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, help_text='Изображение статьи', upload_to='images/article_img'),
        ),
    ]