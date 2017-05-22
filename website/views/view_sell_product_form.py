from django.shortcuts import render
from website.forms.form_product import ProductForm
from website.models.models import Product

def sell_product(request):
    if request.method == 'GET':
        template_name = 'product/create.html'
        product_form = ProductForm()
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        form_data = request.POST
        error_message = None

        if int(form_data['quantity']) < 1:
            error_message = 'Please enter a positive number into quantity.'

        if float(form_data['price']) < 0.01:
            error_message = 'Please enter a positve number into price.'

        if error_message is not None:
            product_form = ProductForm()
            template_name = 'product/create.html'
            return render(request, template_name, { 'product_form': product_form, 'error_message': error_message })
        
        p = Product(
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            quantity = form_data['quantity'],
        )

        p.save()
        template_name = 'product/product_details.html'
        return render(request, template_name, {'product': form_data})