from django.db import models
from user.models import User

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


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Имя')
    total_price = models.PositiveIntegerField(verbose_name='Итоговая сумма')
    address = models.CharField(max_length=255, verbose_name='Aдресс')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now=True)
    code = models.UUIDField(unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.address}'
    

class OrderItem(models.Model):
    product = models.ForeignKey(to=NewBalance, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product} {self.order}'