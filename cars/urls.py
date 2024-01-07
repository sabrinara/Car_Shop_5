from django.urls import path
from . import views

urlpatterns = [
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
]