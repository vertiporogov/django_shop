from django.shortcuts import render

from catalog.models import Category, Product


def home(request):

    context = {
        'object_list': Category.objects.all(),
        'title': 'Магазин всего - Главная'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contact.html', context)


def products(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'Товар - {product_item.name}'
    }

    return render(request, 'catalog/products.html', context)

def product_detail(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товар категории - {category_item.name}'
    }

    return render(request, 'catalog/product_detail.html', context)
