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
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),

    # Auth actions
    path('logindata/', views.logindata, name='logindata'),
    path('register/', views.register, name='register'),

    # Dashboard
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('home1/<int:pk>/', views.home1, name='home1'),

    # Admins page
    path('admins/', views.admins, name='admins'),

    # Student-Specific Book Views
    path('profile/', views.profile, name='profile'),
    path('profile1/<int:pk>/', views.student_profile, name='profile1'),
    path('first1/<int:pk>/', views.student_books_first, name='first1'),
    path('last1/<int:pk>/', views.student_books_last, name='last1'),
    path('all1/<int:pk>/', views.student_books_all, name='all1'),
    path('asc1/<int:pk>/', views.student_books_asc, name='asc1'),
    path('desc1/<int:pk>/', views.student_books_desc, name='desc1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
