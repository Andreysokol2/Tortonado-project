from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
         return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)  # буквенный тип поля
    price_per_kilogram = models.DecimalField(max_digits=10, decimal_places=0,blank=True, null=True, default=0)  # price * nub
    description = models.TextField(blank=True, null=True, default=None)    #описание
    main_image1 = models.ImageField(upload_to='media/products_images', null=True)
    short_description = models.TextField(blank=True, null=True, default=None, max_length=50)  #описание
    structure = models.TextField(blank=True, null=True, default=None)  # описание
    discount = models.IntegerField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    creted = models.DateTimeField(auto_now_add=True, auto_now=False) #время создания
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)#время обновления




    def __str__(self):
         return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products_images')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    creted = models.DateTimeField(auto_now_add=True, auto_now=False)  # время создания
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # время обновления





    # def __str__(self):
    #     return "%s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

