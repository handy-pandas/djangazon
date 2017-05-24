from django.test import TestCase, Client
from website.models.models import *
from website.views.view_category_products import *
from django.urls import reverse


# Example
# Example ends

class CategoryViewTests(TestCase):
	# Create your tests here.
	def test_list_category_products(self):
		seller = User.objects.create(username="test_user")
		category = Category.objects.create(name="test_category")
		Product.objects.create(seller=seller, title="Test", description="Please work buddy!", price="7", quantity="1", category=category)
		Product.objects.create(seller=seller, title="Test1", description="Please work buddy!", price="7", quantity="1", category=category)
		response = self.client.get(reverse('website:category_products', args=[category.id]))
		self.assertQuerysetEqual(
		response.context['products'],
		['<Product: Test>', '<Product: Test1>']
		)

class ProductArttributeTests(TestCase):
	def test_if_product_detail_view_has_title_description_price_quantity(self):
		seller = User.objects.create(username="test_user")
		category = Category.objects.create(name="test_category")
		product = Product.objects.create(seller=seller, title="Test", description="Please work buddy!", price="7", quantity="1", category=category)
		response = self.client.get(reverse('website:product_details', args=[product.id]))
		self.assertContains(
		response, product.title
		)
		self.assertContains(
		response, product.description
		)
		self.assertContains(
		response, product.price
		)
		self.assertContains(
		response, product.quantity
		)


# live server TestCase
# test fixtures