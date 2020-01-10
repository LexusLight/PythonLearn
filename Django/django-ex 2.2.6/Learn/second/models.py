from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12, help_text="Никнейм", unique="true")
    realname = models.CharField(max_length=24, help_text="Имя")
    def __str__(self):
        return self.username

class Message(models.Model):
    id_user = models.ForeignKey(User, on_delete="CASCADE")
    message = models.TextField(max_length = 300)
    def __str__(self):
        return (self.id_user + self.message)
