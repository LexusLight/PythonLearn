from django.db import models

# Create your models here.

class FromForm(models.Model):
    form_text = models.CharField(max_length=300, help_text="То что мы берём из формы - попадает сюда")
    def __str__(self):
        return self.form_text
