"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    
        # Dashboard
    path('home1/<int:pk>/', views.home1, name='home1'),
    path('about1/<int:pk>/', views.about1, name='about1'),
    path('service1/<int:pk>/', views.service1, name='service1'),
    path('registration1/<int:pk>/', views.registration1, name='registration1'),
    path('user_dashboard1/<int:pk>/', views.user_dashboard1, name='user_dashboard1'),
    path('admin_dashboard1/<int:pk>/', views.admin_dashboard1, name='admin_dashboard1'),
        
    path('logindata/', views.logindata, name='logindata'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    
    path('allquery/', views.allquery, name='allquery'),
    path('userallquery/<int:pk>/', views.userallquery, name='userallquery'),
    path('queryres/<int:pk>/', views.queryres, name='queryres'),
    path('newquery/<int:pk>/', views.newquery, name='newquery'),
    
    path('edituser/<int:pk>/', views.edituser, name='edituser'),
    path('deleteuser/<int:pk>/', views.deleteuser, name='deleteuser'),
    path('edituserdata/<int:pk>/', views.edituserdata, name='edituserdata'),
    path('editquery/<int:pk1>/<int:pk>/', views.editquery, name='editquery'),
    path('deletequery/<int:pk1>/<int:pk>/', views.deletequery, name='deletequery'),
    path('edituserquery/<int:pk1>/<int:pk>/', views.edituserquery, name='edituserquery'),

    path('first1/', views.first1, name='first1'),
    path('last1/', views.last1, name='last1'),
    path('asc1/', views.asc1, name='asc1'),
    path('desc1/', views.desc1, name='desc1'),
    
    path('search/', views.search, name='search'),
    
    path('searchall/', views.searchall, name='searchall'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

