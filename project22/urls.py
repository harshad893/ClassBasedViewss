"""project22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(),name='Cbv_string'),
    path('fbv_template/',fbv_template,name='fbv_template'),
    path('Cbv_template/',Cbv_template.as_view(),name='Cbv_template'),
    path('fbv_form/',fbv_form,name='fbv_form'),
    path('Cbv_form/',Cbv_form.as_view(),name='Cbv_form'),
    path('Cbv/',Cbv.as_view(),name='Cbv'),
]
