from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime
from .models import ProductCategory, Product


def get_current_basket(current_user):
    if current_user.is_authenticated:
        items = Basket.objects.filter(user=current_user)
    else:
        items = None

    return items


def main(request: HttpRequest):
    title = 'главная'

    products = Product.objects.all()

    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products,
        'basket': get_current_basket(request.user)
    })


def products(request: HttpRequest, id=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if id is not None:
        same_products = Product.objects.filter(category__pk=id)
    else:
        same_products = Product.objects.all()

    provider = Paginator(same_products, 2)

    try:
        products_provider = provider.page(page)
    except PageNotAnInteger:
        products_provider = provider.page(1)
    except EmptyPage:
        products_provider = provider.page(provider.num_pages)

    # if request.is_ajax():
    #     return JsonResponse(products_provider)

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_menu': links_menu,
        'provider': products_provider,
        'basket': get_current_basket(request.user)
    })


def product_detail(request: HttpRequest, id=None):
    # if id is not None:
    # item = Product.objects.get(pk=id)
    item = get_object_or_404(Product, pk=id)
    same_products = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
    links_menu = ProductCategory.objects.all()

    context = {
        'title': f'Товар: {item.name}',
        'item': item,
        'products': same_products,
        'links_menu': links_menu,
        'basket': get_current_basket(request.user)
    }

    return render(request, 'mainapp/details.html', context)


def contact(request: HttpRequest):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]

    return render(request, 'mainapp/contact.html', {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
    })
