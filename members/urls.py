from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('login_user',views.login_user,name='user-login'),
    path('register',views.Register,name='Register'),
    path('logout',views.logout_user,name='user-logout'),
]