"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app1 import views as v1 
from app2 import views as v2
from app3 import views as v3
from app4 import views as v4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', v1.app1, name='app1' ),
    path('app2/', v2.app2, name='app2' ),
    path('app3/', v3.app3, name='app3' ),
    path('app4/', v4.app4, name='app4' ),
]
