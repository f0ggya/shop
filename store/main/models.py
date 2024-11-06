from django.db import models
from django.contrib.auth.models import User

class Shop_info(models.Model):
    name = models.CharField('Название магазина', max_length=255)
    img = models.ImageField('Лого')
    url = models.CharField('Ссылка', max_length=255)
    
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField('Название продукта', max_length=255)
    img = models.ImageField('Картинка продукта')
    description = models.TextField('Описание продукта', max_length=255)
    shop = models.ForeignKey('main.Shop_info', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        
    def __str__(self):
        return self.name

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cart_products = models.JSONField('Продукты в корзине')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "корзины"
        
    def __str__(self):
        return self.owner.username
    
    


