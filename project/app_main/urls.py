from django.urls import path
from django.contrib.auth import views 
from . import views

urlpatterns = [
    path('permissoes/', views.user_permissions, name='permissoes'),
    path('busca/', views.busca, name='busca'),
    path('editor/', views.editor, name='editor'),
    
    ## test ##
    path('editor/<int:id>', views.editor_id, name='editor_id')
]
