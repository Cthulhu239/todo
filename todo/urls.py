from django.urls import path
from . import views

urlpatterns = [
    path('task_list/', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),  # <-- Add this line
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]



