from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'photo',)
    success_url = reverse_lazy('blog:home')

    # def form_valid(self, form):
    #     if form.is_valid:
    #         new_blog = form.save()
    #         new_blog.slug = slugify(new_blog.title)
    #         new_blog.save()
    #
    #     return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Магазин всего - Главная'
    }
