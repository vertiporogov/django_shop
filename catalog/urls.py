from django.urls import path

from catalog.views import home, contacts, products, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('<int:pk>/product_detail/', product_detail, name='product_detail'),
]
