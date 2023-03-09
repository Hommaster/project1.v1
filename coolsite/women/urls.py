from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('posts/<slug:post_slug>/', ShowPost.as_view(), name='posts'),
    path('cats/<slug:cat_slug>', WomenCats.as_view(), name='category'),
]
