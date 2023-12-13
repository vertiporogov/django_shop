from django.urls import path

from catalog.views import home, contact

urlpatterns = [
    path('', contact, name='contact'),
    path('contact/', contact, name='contact'),
]
