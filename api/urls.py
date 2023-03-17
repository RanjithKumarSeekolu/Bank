from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'api/v1/getbanks/', views.get_banks, name='get_banks'),
    path(r'api/v1/ifsc/<str:ifsc_code>/', views.get_details, name='get_details'),
    path(r'setup', views.setup, name= "setup"),
]
