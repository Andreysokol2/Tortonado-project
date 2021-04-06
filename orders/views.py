from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket

def basket_adding(request):
    print('Views is go')
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    is_delete = data.get("is_delete")
    print(is_delete)
    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
        print('удаляю')
    else:
        apps = data.get('apps')
        weight = data.get('weight')
        total_price = data.get("total_price")
        decorations = data.get("decorations")
        new_product = ProductInBasket.objects.create(session_key = session_key,product_id = product_id, is_active = True, decorations = decorations, apps = str(apps),total_price= total_price, weight = weight)
        print(123)

     #common code for 2 cases
    products_total_nub = ProductInBasket.objects.filter(session_key=session_key, is_active = True).count()
    return_dict["products_total_nub"] = products_total_nub
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nub = products_in_basket.count()
    return_dict["products"] = list()

    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key = session_key, is_active = True)
    return render(request, 'orders/checkout.html', locals())
