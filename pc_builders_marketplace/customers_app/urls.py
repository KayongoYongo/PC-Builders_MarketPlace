from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from views import sign_up_page

urlpatterns = [
    path('sign_up', sign_up_page, name='sign_up_page'),
]