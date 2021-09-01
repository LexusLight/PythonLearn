from django.contrib import admin
from .models import Article,Header,Quote,Paragraph,Image

admin.site.register(Article)
admin.site.register(Header)
admin.site.register(Paragraph)
admin.site.register(Image)
admin.site.register(Quote)
# from .models import User,Message

# Register your models here