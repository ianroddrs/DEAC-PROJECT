from django.urls import path
from django.contrib.auth import views 
from . import views

urlpatterns = [
    path('permissions/', views.user_permissions, name='permissions'),
    path('busca/', views.busca, name='busca'),
    
    ## test ##
    path('editor/', views.edit, name='editor'),
]
