from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name='home'),
    path('Register/', views.Register, name='register'),
    path('Existing/', views.Existing, name='Existing'),


]
