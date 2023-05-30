from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('home/', views.home, name='home'),
    path('sair/', views.sair, name='sair'),

    ## test ##
    path('busca/', views.busca, name='busca'), 
    path('editar/', views.edit, name='editar'),
]
