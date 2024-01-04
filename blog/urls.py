from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, HomeView, BlogUpdateView, BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home2'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('list/', BlogListView.as_view(), name='list_blog'),
]
