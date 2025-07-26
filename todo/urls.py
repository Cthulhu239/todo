from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),      # /tasks/
    path('add/', views.task_add, name='task-add'),    # /tasks/add/
    path('delete/<int:id>/', views.task_delete, name='task-delete'),  # /tasks/delete/1/
]
