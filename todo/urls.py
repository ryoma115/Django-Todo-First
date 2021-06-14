from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList, name='list'),
    path('detail/<int:pk>/', views.TodoDetail, name='detail'),
    path('create/', views.TodoCreate, name='create'),
    path('delete/<int:pk>/', views.TodoDelete, name='delete'),
    path('update/<int:pk>/', views.TodoUpdate, name='update'),
]
