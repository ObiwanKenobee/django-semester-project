from django.urls import path
from . import views

app_name = 'observatory'

urlpatterns = [
    path('', views.home, name='home'),
    path('signals/', views.signals, name='signals'),
    path('signals/<int:pk>/', views.signal_detail, name='signal_detail'),
    path('about/', views.about, name='about'),
]
