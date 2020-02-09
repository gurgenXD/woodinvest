from uuid import uuid1
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from core.models import SEO


class Product(SEO):
    category = models.CharField(max_length=250, verbose_name='Категория')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
    desc = models.TextField(verbose_name='Описание')
    short_desc = models.TextField(verbose_name='Краткое описание')
    features = models.TextField(verbose_name='Характеристики')
    options = models.TextField(verbose_name='Доп. услуги')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_main_image(self):
        main_images = self.images.filter(is_main=True)
        if main_images.exists():
            main_image = main_images.first()
        else:
            main_image = self.images.first()
        return main_image


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/products/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')

    image_big = ImageSpecField(source='image',
                               processors=[ResizeToFill(690, 460)],
                               format='JPEG',
                               options={'quality': 90})

    image_medium = ImageSpecField(source='image',
                               processors=[ResizeToFill(530, 350)],
                               format='JPEG',
                               options={'quality': 90})
    
    image_small = ImageSpecField(source='image',
                               processors=[ResizeToFill(83, 83)],
                               format='JPEG',
                               options={'quality': 90})


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return '{0}'.format(self.id)
