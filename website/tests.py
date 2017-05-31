from django.test import TestCase, Client
from website.models.models import *
from website.views.view_category_products import *
from django.urls import reverse

# Test 1
# Verify that when a specific product category view (e.g. Electronics) 
# is requested,
 # that there are products in the response context
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

# Verify that when n products are added to an order that the Order Summary view has those products in the response context
# Test 2
class OrderSummaryViewTests(TestCase):
    def test_view_order(self):
        c = Client()
        seller = User.objects.create(username="test_user_12", password="thankyouadam1")
        category = Category.objects.create(name="test_category")
        product = Product.objects.create(seller=seller, title="Test12", description="Please work buddy!", price="7", quantity="1", category=category)
        product_2 = Product.objects.create(seller=seller, title="Test12", description="Please work buddy!", price="7", quantity="1", category=category)
        order_yo = Order.objects.create(user=seller, payment_id=None)
        ProductOrder.objects.create(order=order_yo, product=product)
        ProductOrder.objects.create(order=order_yo, product=product_2)
        logged_in = c.force_login(seller, backend=None)
        response = c.get(reverse('website:order'))
        self.assertContains(response, product)
        self.assertContains(response, product_2)

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

# Verify that the Payment Types view for a customer has all of the payment types in the request context
# Test 6
class PaymentViewTests(TestCase):
    def test_payments_show_in_payments_view(self):
        c = Client()
        customer = User.objects.create(username="test_user_1")
        payment = Payment.objects.create(name='Visa', account_number=1234567, user=customer, is_active=1)
        logged_in = c.force_login(customer, backend=None)
        response = c.get(reverse('website:profile/view_payments'))
        self.assertContains(
            response, payment.name
        )




