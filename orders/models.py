from django.db import models
from products.models import Product
from django.db.models.signals import post_save

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)  # буквенный тип поля
    is_active = models.BooleanField(default=True)

    creted = models.DateTimeField(auto_now_add=True, auto_now=False) #время создания
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)#время обновления




    def __str__(self):
         return "%s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы заказа'
class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=3, default=0)  # total price for all products
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)  # буквенный тип поля
    customer_email = models.EmailField(blank=True, null=True, default=None)    #поле базы с типом данных почты
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    coments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    creted = models.DateTimeField(auto_now_add=True, auto_now=False) #время создания
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)#время обновления




    def __str__(self):
        return "%s" % self.customer_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)   #ссыка
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(default=True)
    apps = models.TextField(blank=True, null=True, default=None)
    decorations = models.TextField(blank=True, null=True, default=None)
    weight = models.IntegerField(blank=True, null=True, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)  #price * nub
    creted = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True) #время создания
    updated = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)#время обновления




    def __str__(self):
        return "%s" % self.product

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в козине'

    # def save(self, *args, **kwargs):
    #     if self.product.discount:
    #         print("Скидка есть")
    #         discount = self.product.discount
    #         price_per_tort = (self.product.price / 100)*(100 - int(discount))
    #     else:
    #         print(self.product.price)
    #         total_price = self.weight * self.product.price_per_kilogram
    #     self.total_price = total_price
    #     self.total_price = int(self.nub) * self.price_per_item
    #
    #     super(ProductInBasket, self).save(*args, **kwargs)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)   #ссыка
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    nub = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=3, default=0)  #price * nub
    creted = models.DateTimeField(auto_now_add=True, auto_now=False) #время создания
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)#время обновления




    def __str__(self):
        return "%s" % self.product

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        if self.product.discount:
            print("Скидка есть")
            discount = self.product.discount
            price_per_item = (self.product.price / 100) * (100 - int(discount))
        else:
            price_per_item = self.product.price
        self.price_per_item = int(price_per_item)

        self.total_price = int(self.nub) * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)
