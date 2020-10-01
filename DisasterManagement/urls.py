from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('VulnerabilityProfile', views.VulnerabilityProfile),
    path('DM_Cycle', views.DM_Cycle),
    path('Earthquake', views.Earthquake),
    path('Tsunami', views.Tsunami),
    path('Flood', views.Flood),
    path('UrbanFloods', views.UrbanFloods),
    path('Landslides', views.Landslides),
    path('Cyclone', views.Cyclone),
    path('HeatWave', views.HeatWave),
    path('Nuclear', views.Nuclear),
    path('Biological', views.Biological),
    path('Chemical', views.Chemical),
    path('Login', views.Login),
    path('SignUp', views.SignUp),
    path('LogOut', views.LogOut),
    path('', include('feedback.urls')),
]
