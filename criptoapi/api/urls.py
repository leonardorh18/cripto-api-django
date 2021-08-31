from django.urls import path
from . import views


urlpatterns = [ 

    path('', views.home, name = 'home'),
    path('getPrice/<str:cripto>', views.getPrice, name = 'getPrice'),
    path('getAllinfo/<str:cripto>', views.getAllinfo, name = 'getAllinfo')
      
]
