from django.shortcuts import render
from website.forms.form_product import ProductForm
from website.models.model_product import Product

def sell_product(request):
    if request.method == 'GET':
        template_name = 'product/create.html'
        product_form = ProductForm()
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        form_data = request.POST
        
        error_message = 1

        if error_message == 1:
            product_form = ProductForm()
            template_name = 'product/create.html'
            return render(request, template_name, {'product_form': product_form, 'error_message': 1})

        p = Product(
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            quantity = form_data['quantity'],
        )
        p.save()
        template_name = 'product/success.html'
        return render(request, template_name, {})