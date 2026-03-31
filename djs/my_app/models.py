from django.db import models

class coment(models.Model):
    # title , about , full_text , data
    title = models.CharField('Користувач',max_length=50)
    about = models.CharField('Опис' , max_length=100)
    full_text = models.TextField('Повна інформація')
    data = models.DateTimeField('Дата публікації')
