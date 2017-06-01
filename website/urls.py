from django.conf.urls import url


# Remember to include your view below
# example: from website.views.view_category import *
from website.views import *

app_name = "website"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_user, name='login'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^sell$', sell_product, name='sell'),
    url(r'^category_products/(?P<category_id>.+?)/$', list_category_products, name='category_products'),
    url(r'^products$', list_products, name='list_products'),
    url(r'^search_products/$', search_products, name='search_products'),    
    url(r'^categories$', category_products, name='categories'),
    url(r'^product_details/(?P<product_id>.+?)/$', product_details, name='product_details'),
    url(r'^order$', view_order, name='order'),
    url(r'^payment$', view_payments, name='payment'),
    url(r'^confirmation$', confirm_order, name='confirmation'),
    url(r'^profile$', profile, name='profile'),
    url(r'^add_payment$', add_payment, name='add_payment'),
    url(r'^profile/view_payments$', view_payments, name='profile/view_payments'),
    url(r'^profile/edit_account$', edit_account, name="profile/edit_account"),
    url(r'^order_history$', view_order_history, name="order_history"),
    url(r'^order_history/(?P<order_id>.+?)/$', view_order_details, name="order_details"),
    url(r'^MyProducts$', my_products, name='my_products'),
    url(r'^profile/edit_account$', edit_account, name="profile/edit_account")
]