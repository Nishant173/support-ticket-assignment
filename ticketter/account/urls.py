from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path(route='home/', view=views.home, name='account-home'),
    path(route='about/', view=views.about, name='account-about'),
    path(route='login/',
         view=auth_views.LoginView.as_view(template_name='account/login.html'),
         name='account-login'),
    path(route='logout/',
         view=auth_views.LogoutView.as_view(template_name='account/logout.html'),
         name='account-logout'),
    path(route='register/', view=views.register, name='account-register'),
]