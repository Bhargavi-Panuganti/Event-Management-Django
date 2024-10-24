"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('members/',include('members.urls')),
    path('members/',include('django.contrib.auth.urls')),
]

admin.site.site_header="My Pannel"
admin.site.site_title="Adminstration"
admin.site.site_title="WELCOME"
# handler404='myproject.views.handler404'
# handler400='myproject.views.handler400'
# handler500='myproject.views.handler500'
