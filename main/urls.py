from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_list, name='user_list'),
    path('user/', views.user_form, name='user_form'),
    path('user/<int:id>/', views.user_form, name='user_edit'),
    path('user/delete/<int:id>/', views.user_delete, name='user_delete'),
    path('api/users/', views.user_list_api, name='user_list_api'),
]
