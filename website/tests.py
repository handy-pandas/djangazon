from django.test import TestCase, Client
from website.models.models import *
from website.views.view_category_products import *
from django.urls import reverse

# Test 1
class CategoryViewTests(TestCase):
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


# Test 3
class ProductDetailViewTests(TestCase):
	def test_product_details(self):
		seller = User.objects.create(username="test_user_1")
		category = Category.objects.create(name="test_category_1")
		product = Product.objects.create(seller=seller, title="Test2", description="Please work buddy!", price="7", quantity="1", category=category)
		response = self.client.get(reverse('website:product_details', args=[product.id]))
		self.assertEqual(response.context['product'], product)

# Test 4
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