from django.contrib import admin
from .models import Categories,Threads,Comments #переносим в админку нужные таблицы

''' Тут мы регистрируем наши модели из базы данных'''

admin.site.register(Categories)
admin.site.register(Threads)
admin.site.register(Comments)

# Register your models here.
