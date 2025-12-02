from django.urls import path
from . import views
#from .views import temp_convert_view


urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('temperature/', views.temperature_view, name="temperature"),
    path('distance/', views.distance_view, name="distance"),
    path('volume/', views.volume_view, name="volume"),
    path('weight/', views.weight_view, name="weight"),
]