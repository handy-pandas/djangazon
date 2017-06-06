from django.contrib.auth.models import *
from django.db.models import Avg
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
        return Product.objects.filter(category=self, is_active=1, quantity__gt=0)[:3]


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

    is_active = models.IntegerField(default=1, choices=options)
    city = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to='images/', blank=True)
    local_delivery = models.BooleanField(default=False)
    city = models.CharField(max_length=50, null=True)


    def sold_count(self):
        return ProductOrder.objects.select_related("order", "product").filter(product=self, order__payment__isnull=False).count()

    def get_count_on_order(self, order_id):
        return ProductOrder.objects.filter(product=self, order=order_id).count()

    def get_rating_for_customer(self, user, order):
        try:
            rating = Rate.objects.get(user=user, product=self, order=order)
            return rating.rate
        except Rate.DoesNotExist:
            return False

    def get_average_rating(self):
        avg_rating = Rate.objects.filter(product=self).aggregate(Avg('rate'))
        if avg_rating['rate__avg'] != None:
            return str(round(avg_rating['rate__avg'], 2))
        else:
            return 'Product has not been rated yet.'

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

def get_cart_items(self):
    order = Order.objects.get(user=self, payment=None)
    return order.get_product_count()

User.add_to_class('get_cart_items', get_cart_items)


class Profile(models.Model):
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def get_average_rating(self, user):
        avg_rating = Rate.objects.select_related("product").filter(product__seller=user).aggregate(Avg('rate'))
        if avg_rating['rate__avg'] != None:
            return str(round(avg_rating['rate__avg'], 2))
        else:
            return 'Your products do not have any ratings.'


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

class Rate(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    rate = models.IntegerField(null=True, blank=True)

class Recommendation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

def get_recommendations_notifications(self):
    notifications = Recommendation.objects.filter(receiver=self)
    return notifications.count()

User.add_to_class('get_recommendations_notifications', get_recommendations_notifications)

