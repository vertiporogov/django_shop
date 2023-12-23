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


def products(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товар'
    }

    return render(request, 'catalog/products.html', context)
