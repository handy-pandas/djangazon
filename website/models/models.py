from django.contrib.auth.models import *
from django.db import models

# Create your models here.
# check data types
# check attributes
# check pks, fks, and join tables

options = (
        (0, 'False'),
        (1, 'True'),
    )

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_products(self):
        return Product.objects.filter(category=self)[:3]


class Payment(models.Model):
    name = models.CharField(max_length=255)
    account_number = models.IntegerField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    is_active = models.IntegerField(default=1, choices=options)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    payment = models.ForeignKey(
        Payment,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField('Product', through='ProductOrder')

    def get_products(self):
        return ProductOrder.objects.filter(order_id=self)

    def get_product_count(self):
        return ProductOrder.objects.filter(order_id=self).count()

class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    is_active = models.IntegerField(default=0, choices=options)
    city = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='productorders'
    )
    quantity = models.IntegerField()

def get_cart_items(self):
    order = Order.objects.get(user=self, payment=None)
    return order.get_product_count()

User.add_to_class('get_cart_items', get_cart_items)


class Profile(models.Model):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class Opinion(models.Model):
    like = models.IntegerField(default=0, choices=options)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )