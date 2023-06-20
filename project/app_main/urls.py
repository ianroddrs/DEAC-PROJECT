from django.urls import path
from django.contrib.auth import views 
from . import views

urlpatterns = [
    path('permissoes/', views.user_permissions, name='permissoes'),
    path('busca/', views.busca, name='busca'),
    
    ## test ##
    path('editor/', views.edit, name='editor'),
]
