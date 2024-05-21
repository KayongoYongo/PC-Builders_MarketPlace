from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.blog_list, name='blog_list'),
    path("create-blog", views.create_blog, name='create_blog'),
]