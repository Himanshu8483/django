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

# # with the help of routers.py in app: 
# from django.contrib import admin
# from django.urls import path, include
# from app.routers import router
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls))
# ]

# without use of routers.py external file in app 
from django.urls import path, include
from app.views import StudentViewSet
from rest_framework import routers

# define the router : 
router = routers.DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
# specify url path for rest_framework 
urlpatterns = [
    path('', include(router.urls))
]