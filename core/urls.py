from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('home/', views.home, name='home'),
    path('sair/', views.sair, name='sair'),
    path('permissions/', views.user_permissions, name='permissions'),


    ## test ##
    path('testing/', views.testing, name='testing'),  
]
