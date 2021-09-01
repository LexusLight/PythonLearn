from django.db import models

# Create your models here.

ID = 1
class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200, unique=True)
    preview_text = models.TextField(verbose_name="Описание статьи", max_length=1000, blank=True)
    preview_image = models.ImageField(upload_to="images/article_img", help_text= "Изображение статьи", blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    parts = models.SmallIntegerField(default=0)
    def __str__(self):
        return str(self.title)

class Image(models.Model):
    id_article = models.ForeignKey("Article", verbose_name = "Статья", on_delete=models.CASCADE, default=ID)
    image = models.ImageField(upload_to="images/article_img",help_text= "Картинка")
    about = models.TextField(verbose_name="Заголовок", max_length=1000)
    position = models.SmallIntegerField(default=0)
    def __str__(self):
        return str(self.image)

class Paragraph(models.Model):
    id_article = models.ForeignKey("Article", verbose_name = "Статья", on_delete=models.CASCADE, default=ID)
    text = models.TextField(verbose_name="Параграф", max_length=5000)
    position = models.SmallIntegerField(default=0)
    def __str__(self):
        return str(self.text)

class Quote(models.Model):
    id_article = models.ForeignKey("Article", verbose_name = "Статья", on_delete=models.CASCADE, default=ID)
    quote = models.TextField(verbose_name="Цитата", max_length=300)
    position = models.SmallIntegerField(default=0)
    def __str__(self):
        return str(self.quote)

class Header(models.Model):
    id_article = models.ForeignKey("Article", verbose_name = "Статья", on_delete=models.CASCADE, default=ID)
    text = models.CharField(verbose_name="Заголовок", max_length=200)
    position = models.SmallIntegerField(default=0)
    def __str__(self):
        return str(self.text)


