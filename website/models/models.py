from django.contrib.auth.models import *
from django.db import models

# Create your models here.
# check data types
# check attributes
# check pks, fks, and join tables

class Category(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.SmallIntegerField()
    is_active = models.SmallIntegerField()
    is_staff = models.SmallIntegerField()
    date_joined = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    name = models.CharField(max_length=255)
    account_number = models.IntegerField()
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class Order(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    payment_id = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
    )


class Product(models.Model):
    seller_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    is_active = models.SmallIntegerField()


class ProductOrder(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )