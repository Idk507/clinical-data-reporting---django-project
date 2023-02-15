"""clinicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from clinicalapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.patientlistview.as_view(template_name = 'patient_list.html'),name ='index'),
    path('create/',views.patientcreateview.as_view(template_name ='patient_form.html')),
    path('update/<int:pk>/',views.patientupdateview.as_view(template_name = 'patient_update.html')),
    path('delete/<int:pk>/',views.patientdeleteview.as_view(template_name = 'patient_delete.html')),
    path('adddata/<int:pk>/',views.adddata),
    path('analyse/<int:pk>/',views.analyse)
]
