from django.contrib import admin
from .models import Place, Info #Для работы с БД 
# Register your models here.
''' Тут мы регистрируем наши модели из базы данных'''
admin.site.register(Place)
admin.site.register(Info)