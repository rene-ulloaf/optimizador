from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('carga_archivo', views.carga_archivo),
    path('datos_archivo', views.datos_archivo),
    path('optimizar', views.optimizar)
]