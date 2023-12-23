from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} ({phone}): {message}')

    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')
