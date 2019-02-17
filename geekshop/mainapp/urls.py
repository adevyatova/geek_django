from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.products, name='index'),  # {% url 'products:index' %}
    path('page/<int:page>/', controller.products, name='page'),  # {% url 'products:page' page=2 %}
    path('<int:id>/', controller.products, name='category'),  # products:category id=1
    path('details/<int:id>/', controller.product_detail, name='details'),  # products:details id=1
]
