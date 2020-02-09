from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    title_index = models.CharField(max_length=250, verbose_name='Название для главной страницы')
    text_index = models.CharField(max_length=250, verbose_name='Описание для главной страницы')
    desc = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title
