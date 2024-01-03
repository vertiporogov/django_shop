from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, HomeView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view, name='create_blog'),
    path('home/', HomeView.as_view(), name='home2'),
]
