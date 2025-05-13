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

    # Public Pages
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),

    # Auth actions
    path('logindata/', views.logindata, name='logindata'),
    path('register/', views.register, name='register'),

    # Dashboard
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('home1/<int:pk>/', views.home1, name='home1'),
    path('about1/<int:pk>/', views.about1, name='about1'),
    path('service1/<int:pk>/', views.service1, name='service1'),
    path('registration1/<int:pk>/', views.registration1, name='registration1'),
    path('admins1/<int:pk>/', views.admins1, name='admins1'),

    # Admins page
    path('admins/', views.admins, name='admins'),

    # Student-Specific Book Views
    path('profile/', views.profile, name='profile'),
    path('profile1/<int:pk>/', views.profile1, name='profile1'),
    path('first1/<int:pk>/', views.first1, name='first1'),
    path('last1/<int:pk>/', views.last1, name='last1'),
    path('all1/<int:pk>/', views.all1, name='all1'),
    path('asc1/<int:pk>/', views.asc1, name='asc1'),
    path('desc1/<int:pk>/', views.desc1, name='desc1'),
    
    
    path('edit/<int:pk1>/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk1>/<int:pk>/', views.delete, name='delete'),
    path('editdata/<int:pk1>/<int:pk>/', views.editdata, name='editdata'),
    
    path('edituser/<int:pk>/', views.edituser, name='edituser'),
    # path('deleteuser/<int:pk>/', views.deleteuser, name='deleteuser'),
    path('edituserdata/<int:pk>/', views.edituserdata, name='edituserdata'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
