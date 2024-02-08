from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, \
    DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm
from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    # form_class = BlogForm
    fields = ('title', 'description', 'photo',)
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:home2')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    permission_required = 'blog.change_blog'

    # fields = ('title', 'description', 'photo',)
    # success_url = reverse_lazy('blog:detail_blog')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail_blog', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Blog
    permission_required = 'blog.view_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    permission_required = 'blog.delete_blog'
    success_url = reverse_lazy('blog:list_blog')


class HomeView(TemplateView):
    template_name = 'blog/home.html'
    extra_context = {
        'title': 'Блогерная'
    }
