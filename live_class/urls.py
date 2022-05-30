"""live_class URL Configuration

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
from live_class.views import template_using_context,template_using_loader,new_familiar,def_template,familiar_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template_using_context/<str:name>/<str:last_name>', template_using_context),
    path('template_using_loader/<str:name>/<str:last_name>', template_using_loader),
    path('new_familiar/<str:nombre>/<str:edad>/<str:fecha_de_nacimiento>',new_familiar),
    path('',def_template),
    path('familiar_info',familiar_info)
]
