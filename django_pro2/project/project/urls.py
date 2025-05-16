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
    path('admins1/<int:pk>/', views.admins1, name='admins1'),
    path('student_dashboard1/<int:pk>/', views.student_dashboard1, name='student_dashboard1'),
    path('admin_dashboard1/<int:pk>/', views.admin_dashboard1, name='admin_dashboard1'),
        
    path('logindata/', views.logindata, name='logindata'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    
    path('allquery/', views.allquery, name='allquery'),
    path('stuallquery/', views.stuallquery, name='stuallquery'),
    path('queryres/<int:pk>/', views.queryres, name='queryres'),
    path('newquery/<int:pk>/', views.newquery, name='newquery'),
    
    path('edituser/<int:pk>/', views.edituser, name='edituser'),
    path('deleteuser/<int:pk>/', views.deleteuser, name='deleteuser'),
    path('edituserdata/<int:pk>/', views.edituserdata, name='edituserdata'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

