from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('getBooks', views.books, name='search')
]
