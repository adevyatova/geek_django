from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.products, name='index'),  # {% url 'products:index' %}
    path('<int:id>/', controller.products, name='category'),  # products:category id=1
]
