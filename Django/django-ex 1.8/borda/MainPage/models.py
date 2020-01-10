from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length = 50, help_text = "Имя категории")
    category_info = models.TextField(help_text = "Описание категории")
    def __str__(self):
        return self.category_name #В админке отображается нормально

class Threads(models.Model):
    category_id = models.ForeignKey(Categories)
    thread_autor = models.CharField(max_length = 30, help_text = "Автор треда")
    thread_name = models.CharField(max_length = 100, help_text = "Имя треда")
    thread_text = models.TextField(help_text = "Текст внутри треда")
    def __str__(self):
        return self.thread_name

class Comments(models.Model):
    thread_id = models.ForeignKey(Threads)
    thread_autor = models.CharField(max_length = 30, help_text = "Автор комментария")
    comment_text = models.TextField(help_text = "Комментарий")
    def __str__(self):
        return self.comment_text
# Create your models here.
