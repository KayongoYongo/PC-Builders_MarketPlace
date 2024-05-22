from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.blog_list, name='blog_list'),
    path("create-blog", views.create_blog, name='create_blog'),
    path('view-blog/<int:id>', views.view_blog, name='view_blog'),
    path('my-blogs/', views.view_my_blogs, name='view_my_blogs' )
]