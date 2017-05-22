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


# class User(models.Model):
#     username = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    # email = models.EmailField(max_length=254)
    # last_login = models.DateTimeField(auto_now=True)
    # is_superuser = models.IntegerField(default=0, choices=options)
    # is_active = models.IntegerField(default=0, choices=options)
    # is_staff = models.IntegerField(default=0, choices=options)
    # date_joined = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    name = models.CharField(max_length=255)
    account_number = models.IntegerField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


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


class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    is_active = models.IntegerField(default=0, choices=options)


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )