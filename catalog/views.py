from django.shortcuts import render
from django.urls import reverse_lazy
# from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView

from catalog.forms import ProductForm
from catalog.models import Category, Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Магазин всего - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()
        return context_data


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('catalog:home')


class ContactView(View):
    template_name = 'catalog/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')

            phone = request.POST.get('phone')

            message = request.POST.get('message')

            print(name, phone, message)

        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context_data
