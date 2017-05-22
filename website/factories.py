"""
bangazon factory to create sample data to seed a database using Faker in lieu of using 
fixtures
"""

import factory
from website.models.models import *

class CategoryFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the category table in the database.

    ----Fields----
    name('word'): fake name of a category

    Author: Adam Myers
    """

    class Meta:
        model = Category
    name = factory.Faker('word')

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
    account_number = factory.Faker('phone_number')
    user = factory.Iterator(User.objects.all())

class OrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order table in the database.

    ----Fields----
    user(Iterator[User]): iterates over user.object.all to pull foreign keys
    user(Iterator[Payment]): iterates over payment.object.all to pull foreign keys

    Author: Adam Myers
    """
    user = factory.Iterator(User.objects.all())
    payment = factory.Iterator(Payment.objects.all())

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

    Author: Adam Myers
    """
    seller = factory.Iterator(User.objects.all())
    title = factory.Faker('word')
    description = factory.Faker('bs')
    price = factory.Faker('random_int')
    quantity = factory.Faker('random_int')
    category = factory.Iterator(Category.objects.all())
    is_active = 1

class ProductOrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product table in the database.

    ----Fields----
    seller(Iterator[User]): iterates over user.objects.all
    name('word'): fake title of a product

    Author: Adam Myers
    """
    product = factory.Iterator(Product.objects.all())
    order = factory.Iterator(Order.objects.all())




