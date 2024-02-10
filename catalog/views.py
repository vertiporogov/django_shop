from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
# from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, CategoryForm
from catalog.models import Category, Product, Version
from catalog.services import get_categories_cache


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Магазин всего - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_categories_cache()
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    # success_url = reverse_lazy('catalog:home')`

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

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


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'

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

        form.instance.owner = self.request.user

        # print(formset.is_valid())
        # print(formset.errors)

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.owner != self.request.user:
            raise Http404
        return self.object


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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'catalog.change_category'

    def get_success_url(self):
        return reverse('catalog:category_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_categories_cache()
        return context_data


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


@login_required
@permission_required('catalog.change_product')
def toggle_published(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_published:
        product_item.is_published = False
    else:
        product_item.is_published = True

    product_item.save()

    return redirect(reverse('catalog:home'))
