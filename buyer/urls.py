from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('buyer/', views.buyer, name='buyer'),
    path('changePassword/', views.change_password, name='password_change'),
    path('changePassword2/', views.change_password2, name='password_change_without_old_password'),
]