"""
bangazon factory to create sample data to seed a database using Faker in lieu of using 
fixtures
"""

import factory
from website.models.models import *
from django.contrib.auth.models import *

class CategoryFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the category table in the database.

    ----Fields----
    name('word'): fake name of a category

    Author: Adam Myers
    """

    class Meta:
        model = Category
    name = factory.Faker('bs')

class UserFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the user table in the database.

    ----Fields----
    username('word'): fake name of a username
    first_name('first_name'): fake first name
    last_name('last_name'): fake last name
    password('word'): fake password
    email('email'): fake email
    last_login('date'): fake date
    is_supervisor: 0
    is_active: 0
    is_staff: 0
    date_joined('date'): fake date

    Author: Adam Myers
    """

    class Meta:
        model = User
    username = factory.Faker('word')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')
    email = factory.Faker('email')
    last_login = factory.Faker('date')
    is_superuser = 0
    is_active = 0
    is_staff = 0
    date_joined = factory.Faker('date')

class PaymentFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the payment table in the database.

    ----Fields----
    name('name'): fake name of a user
    account_number('phone_number'): fake account number
    user_id(Iterator[User]): iterates over user.object.all to pull foreign keys

    Author: Adam Myers
    """

    class Meta:
        model = Payment
    name = factory.Faker('name')
    account_number = factory.Faker('random_int', min=1000000000000000, max=9999999999999999)
    user = factory.Iterator(User.objects.all())
    is_active = 1

class OrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order table in the database.

    ----Fields----
    user(Iterator[User]): iterates over user.object.all to pull foreign keys
    payment(Iterator[Payment]): iterates over payment.object.all to pull foreign keys

    Author: Adam Myers
    """
    class Meta:
        model = Order
    user = factory.Iterator(User.objects.all())
    payment = factory.Iterator(Payment.objects.all())

class InCompleteOrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order table in the database.

    ----Fields----
    user(Iterator[User]): iterates over user.object.all to pull foreign keys
    payment(Iterator[Payment]): iterates over payment.object.all to pull foreign keys

    Author: Adam Myers
    """
    class Meta:
        model = Order
    user = factory.Iterator(User.objects.all())

class ProductFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product table in the database.

    ----Fields----
    seller(Iterator[User]): iterates over user.objects.all
    name('word'): fake title of a product
    description('bs'): fake description of a product
    price('random_int'): fake price of a product
    quantity('random_int'): fake quantity of a product
    category(Iterator[Category]): iterates over category.objects.all
    is_active: 0
    city: fake name of a city
    photo: fake photo id number

    Author:
        Talbot Lawrence
        Adam Myers
    """
    class Meta:
        model = Product
    seller = factory.Iterator(User.objects.all())
    title = factory.Faker('word')
    description = factory.Faker('bs')
    price = factory.Faker('random_int', min=1, max=100)
    quantity = factory.Faker('random_int', min=10, max=50)
    category = factory.Iterator(Category.objects.all())
    is_active = 1
    city = factory.Faker('city')
    image_path = factory.Faker('file_path', depth=1, category=None, extension=None)
    

class ProductOrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product table in the database.

    ----Fields----
    product(Iterator[Product]): iterates over product.objects.all
    order(Iterator[Order]): iterates over order.objects.all
    quantity('random_int'): fake quantity of an order

    Author: Talbot Lawrence
            Adam Myers
    """
    class Meta:
        model = ProductOrder
    product = factory.Iterator(Product.objects.all())
    order = factory.Iterator(Order.objects.all())
    quantity = factory.Faker('random_int', min=10, max=50)


class ProfileFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the opinion table in the database.

    ----Fields----
    phone_number('(615)444-4765'): fake phone number for a customer
    address('123 Nick Nash Blvd'): fake address for a customer
    city('Smyrna'): fake city for a customer
    state('TN'): fake state number for a customer
    zipcode('35223-1234'): fake zip code for a customer
    user(Iterator[Order]): iterates over user.objects.all

    Author: Talbot Lawrence
    """
    class Meta:
        model = Profile
    phone_number = factory.Faker('phone_number')
    address = factory.Faker('address')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    zipcode = factory.Faker('postalcode')
    user = factory.Iterator(User.objects.all())


class OpinionFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the opinion table in the database.

    ----Fields----
    product(Iterator[Product]): iterates over product.objects.all
    user(Iterator[Order]): iterates over user.objects.all
    like: 1 implies you like the product

    Author: Talbot Lawrence
    """
    class Meta:
        model = Opinion
    like = 1
    product = factory.Iterator(Product.objects.all())
    user = factory.Iterator(User.objects.all())