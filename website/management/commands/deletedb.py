"""
bangazon custom command to build database
"""

import os
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


    Author: Talbot Lawrence, Adam Myers
    """

    def handle(self, *args, **options):
        os.system('find . -path "/website/migrations/*.py" -not -name "__init__.py" -delete;')  #deletes all of the .py files in the migrations directory except for the __init__.py file.
        os.system('find . -path "/website/migrations/*.pyc"  -delete;')  #deletes all of the .pyc files in the migrations directory.
        os.system('rm db.sqlite3;')  #deletes the database file.
        #os.system('python manage.py makemigrations website;')  #creates the migration.
        #os.system('python manage.py migrate;')  #runs the migration.  This will delete all of the data in your database.