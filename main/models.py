from django.db import models

class Category(models.Model):
    """Категория товара"""
    title = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self) -> str: # dunder method
        return f'{self.title}'
    
class NewBalance(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products')
    price = models.PositiveIntegerField(verbose_name='цена')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'


class Images(models.Model):
    sneakers = models.ForeignKey(to=NewBalance, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sneakers_images',verbose_name='Изображение')