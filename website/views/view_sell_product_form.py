from django.shortcuts import render
from website.forms.form_product import ProductForm
from website.models.models import Product, Category

def sell_product(request):
    """This function allows the user to add a product to the Product table to be sold.
    
    Arguments:
        request: django request format containing information about the request.
    
    Returns:
        request: django request format containing information about the request.
        template_name (HTML): The webpage's structure
        product_form (Dict): This is the form information formating a product information

    Author:
        Adam Myers
        Nick Nash
    """
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
            error_message = 'Please enter a positive number into price.'

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
            category = Category.objects.get(pk=form_data['category']),
            local_delivery = form_data['local_delivery'],
            city = form_data['city']
        )
        try:
            p.local_delivery = True

        except:
            p.local_delivery = False

            
        p.save()
        template_name = 'product/product_details.html'
        return render(request, template_name, { 'product': p })