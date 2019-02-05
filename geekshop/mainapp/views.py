from django.shortcuts import render
from django.http import HttpRequest

import datetime
from .models import ProductCategory, Product


def main(request: HttpRequest):
    title = 'главная'

    products = Product.objects.all()

    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products
    })


def products(request: HttpRequest, id=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    })


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
