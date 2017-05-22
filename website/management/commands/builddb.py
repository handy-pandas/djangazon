"""
bangazon custom command to build database
"""

from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
from website.factories import *

class Command(BaseCommand):
    """
    Defines the command 'builddb', which is a shortcut for running
    the necessary shell commands to generate our database's tables and
    load our data to them via Faker. These commands are, in order:
    1. python manage.py makemigrations api
    2. python manage.py migrate
    3. (Factory Calls): Category, User, Payment, Product, ProductOrder


    Author: Adam Myers
    """

    def handle(self, *args, **options):
        management.call_command('makemigrations')
        management.call_command('migrate')
        CategoryFactory.create_batch(size=10)
        UserFactory.create_batch(size=10)
        PaymentFactory.create_batch(size=10)
        OrderFactory.create_batch(size=10)
        ProductFactory.create_batch(size=20)
        ProductOrderFactory.create_batch(size=10)
        
