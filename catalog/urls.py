from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ProductListView, ProductDetailView, ContactView, \
    ProductCreateView, ProductUpdateView, CategoryUpdateView, CategoryListView, CategoryDetailView, \
    toggle_published

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('catalog/products/<int:pk>/', ProductListView.as_view(), name='products_list'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('catalog/category/', CategoryListView.as_view(), name='category_list'),
    path('view/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('activity/<int:pk>/', toggle_published, name='toggle_published'),
]
