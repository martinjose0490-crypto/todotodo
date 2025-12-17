from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('view/<int:pk>/', views.todo_detail, name='todo_detail'), # 'pk' or 'id'
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]