from django.conf.urls import url

# Remember to include your view below
# example: from website.views.view_category from *
from website.views.views import *
from website.views.product_details_view import *
from website.views.view_sell_product_form import sell_product
from website.views.views_product_list import list_products


app_name = "website"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_user, name='login'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^sell$', sell_product, name='sell'),
    url(r'^products$', list_products, name='list_products'),
    url(r'^product_details$', product_details, name='product_details')
]