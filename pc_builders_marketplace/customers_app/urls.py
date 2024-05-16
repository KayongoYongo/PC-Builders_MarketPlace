from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path('sign_up', views.sign_up_page, name='sign_up_page'),
    path('log_in', views.log_in_page, name='log_in_page'),
    path('logout', views.logout_page, name='logout_page')
]