# Welcome to Bangazon

This web application is the source code for the Bangazon e-commerce web site. It is powered by Python and Django.

Students, you are inheriting a basic implementation that provides the following features:

1. User registration 
1. User login 
1. User logout 
1. Adding a product 
1. Listing products

Please consult the backlog of issues and work with your product owner to implement the top priority tickets for your sprints.

## To begin work

1. Fork this repository into your team's Github organization.
1. Alert your manager when this is complete and all backlog issues will be imported into your fork.
1. Each teammate should clone the repository.
1. In the `djangazon` directory that gets created, run the migrations with `python manage.py migrate`

## Helpful Resources

### Django Models and Migrations

Using the requirements above create a [model](https://docs.djangoproject.com/en/1.10/topics/db/models/) for each resource, and use [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/) to ensure your database structure is up to date.

### Templates

[Django template language](https://docs.djangoproject.com/en/1.10/ref/templates/language/)

### Form Helpers

Django, like Angular, has many built-in [helper tags and filters](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/) when building the site templates. We strongly recommend reading this documentation while building your templates.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django:
```
pip install django
```

Install Pillow:
```
pip install Pillow
```

### Installing
Clone repo:

```
git clone https://github.com/handy-pandas/djangazon.git
cd djangazon
```
Setting up the database:
```
python manage.py builddb 
```
Run project in browser:

```
python manage.py runserver
```
In your browser you should see somthing like this:
![home screen](images/djangazon-home.jpg?raw=true)

## Running the tests
Navigate to the djangazon directory and type this command:
```
python manage.py test website
```

## Deployment
No additional resources required.
## Built With

* [Python](http://www.dropwizard.io/1.0.2/docs/) - Main Language
* [Django](http://www.dropwizard.io/1.0.2/docs/) - The framework used
* [pip](https://maven.apache.org/) - Dependency Management
* [pip](https://maven.apache.org/) - Dependency Management
* [grunt](https://gruntjs.com/) - Javascript Task Runner
* [sass](http://sass-lang.com/) - Styling


## Authors

* **Adam Myers** - [ANMyers](https://github.com/ANMyers)
* **Angela Lee** - [leead4](https://github.com/leead4)
* **Nick Nash** - [thenicknash](https://github.com/thenicknash)
* **Talbot Lawrence** - [talbotlawrence](https://github.com/talbotlawrence)
* **William Caldwell** - [wocaldwell](https://github.com/wocaldwell)


## Acknowledgments
"Thank you all and GOOD NIGHT!" - Every Musician Ever
