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
from app.views import sensor, create_sensor, create, view_sensor, edit_sensor, update_sensor, delete_sensor, \
    home_planta, form_planta, create_planta, view_planta, edit_planta, update_planta, delete_planta, register_user, \
    create_user, dologin, login_panel, logouts, measurer, simulator_measurer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/', sensor),
    path('create_sensor/', create_sensor),
    path('create/', create, name='create'),
    path('view_sensor/<int:pk>/', view_sensor, name='view_sensor'),
    path('edit_sensor/<int:pk>/', edit_sensor, name='edit_sensor'),
    path('update_sensor/<int:pk>/', update_sensor, name='update_sensor'),
    path('delete_sensor/<int:pk>/', delete_sensor, name='delete_sensor'),
    path('', home_planta, name='home_planta'),
    path('form_planta/', form_planta, name='form_planta'),
    path('create_planta/', create_planta, name='create_planta'),
    path('view_planta/<int:pk>/', view_planta, name='view_planta'),
    path('edit_planta/<int:pk>/', edit_planta, name='edit_planta'),
    path('update_planta/<int:pk>/', update_planta, name='update_planta'),
    path('delete_planta/<int:pk>/', delete_planta, name='delete_planta'),
    path('register_user/', register_user),
    path('create_user/', create_user),
    path('login/', login_panel),
    path('dologin/', dologin),
    path('logouts/', logouts),
    path('measurer/', measurer),
    path('simulator/', simulator_measurer),

]
