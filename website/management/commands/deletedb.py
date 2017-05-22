import os

os.system('find . -path "/website/migrations/*.py" -not -name "__init__.py" -delete;')  #deletes all of the .py files in the migrations directory except for the __init__.py file.
os.system('find . -path "/website/migrations/*.pyc"  -delete;')  #deletes all of the .pyc files in the migrations directory.
os.system('rm db.sqlite3;')  #deletes the database file.
#os.system('python manage.py makemigrations website;')  #creates the migration.
#os.system('python manage.py migrate;')  #runs the migration.  This will delete all of the data in your database.