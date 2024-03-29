# Generated by Django 3.0.2 on 2020-06-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('position', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Картинка', upload_to='')),
                ('about', models.TextField(max_length=1000, verbose_name='Заголовок')),
                ('position', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Параграф')),
                ('position', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=300, verbose_name='Цитата')),
                ('position', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок')),
                ('preview_text', models.TextField(blank=True, max_length=1000, verbose_name='Описание статьи')),
                ('image', models.ImageField(blank=True, help_text='Изображение статьи', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('parts', models.SmallIntegerField(default=0)),
                ('id_header', models.ManyToManyField(blank=True, to='D.Header', verbose_name='Цитаты')),
                ('id_images', models.ManyToManyField(blank=True, to='D.Image', verbose_name='Картинки')),
                ('id_paragraph', models.ManyToManyField(blank=True, to='D.Paragraph', verbose_name='Параграфы')),
                ('id_quote', models.ManyToManyField(blank=True, to='D.Quote', verbose_name='Цитаты')),
            ],
        ),
    ]
