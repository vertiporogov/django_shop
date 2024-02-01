from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
# from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('catalog:home')`

    def get_success_url(self):
        return reverse('catalog:products_list', args=[self.object.category.pk])

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         formset = VersionFormset(self.request.POST)
    #     else:
    #         formset = VersionFormset()
    #
    #     context_data['formset'] = formset
    #     return context_data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('catalog:home')`

    def get_success_url(self):
        return reverse('catalog:products_list', args=[self.object.category.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)



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
