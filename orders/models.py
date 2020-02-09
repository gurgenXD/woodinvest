from django.db import models
from services.models import Service


class Region(models.Model):
    title = models.CharField(max_length=250, verbose_name='Регион')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.title


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', related_name='orders')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион', related_name='orders')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    material = models.CharField(max_length=250, verbose_name='Вид сырья и объём')
    deadline = models.CharField(max_length=250, verbose_name='Сроки оказания услуг')
    contact = models.CharField(max_length=250, verbose_name='Контактное лицо')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=250, verbose_name='E-mail')
    note = models.TextField(verbose_name='Примечание')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{0} - {1}'.format(self.service.title, self.contact)

