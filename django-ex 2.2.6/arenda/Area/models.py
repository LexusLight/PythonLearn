from django.db import models

# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length = 40, help_text = "Название арендуемого места")
    place_adress = models.TextField(help_text = "Адрес места")
    place_area = models.TextField(help_text = "Рамки по площади")
    def __str__(self):
        return self.place_name #Стас, эта штука при инициализации в админке помогает

class Info(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    info_second_name = models.CharField(max_length = 50, help_text = "Резервное поле для отображения")
    info_maplink = models.TextField(help_text = "Ссылка на карту")
    info_price = models.TextField(help_text = "Расценки")
    def __str__(self):
        return self.info_second_name