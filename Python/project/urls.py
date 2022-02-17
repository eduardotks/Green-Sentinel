"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.views import sensor, create_sensor, create, view_sensor, update_sensor, update, delete_sensor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/', sensor),
    path('create_sensor/', create_sensor),
    path('create/', create, name='create'),
    path('view_sensor/<int:pk>/', view_sensor, name='view_sensor'),
    path('update_sensor/<int:pk>/', update_sensor, name='update_sensor'),
    path('update/<int:pk>/', update, name='update'),
    path('delete_sensor/<int:pk>/', delete_sensor, name='delete_sensor'),
]
