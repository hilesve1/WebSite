from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Класс для таблиц в бд
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique = True) #чтобы названия не совпадали)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name = 'Автор', on_delete=models.CASCADE)
    #pic = models.ImageField('Добавить фото', upload_to='user_images',  default='white.png')


    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
    #описание статьи
    def __str__(self):
        return f' {self.title}'

    #чтобы убрать s на конце и таблица была на русском
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
