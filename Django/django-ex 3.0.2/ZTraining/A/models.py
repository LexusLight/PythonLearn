from django.db import models


class Pages(models.Model):
    page_name = models.TextField(help_text="Название раздела")
    page_link = models.TextField(help_text="Ссылка на раздел")
    def __str__(self):
        return(self.page_name)
# Create your models here.