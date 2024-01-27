from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ProductListView, ProductDetailView, ContactView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('catalog/products/<int:pk>/', ProductListView.as_view(), name='products_list'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create')
]
