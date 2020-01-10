from django.contrib import admin
from .models import User,Message

# Register your models here.
admin.site.register(Message)
admin.site.register(User)