from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField() 
    date = models.DateField()
    imagelink = models.CharField(max_length = 50, default="glad.png")
    def __str__(self):
        return self.title
# Create your models here.
