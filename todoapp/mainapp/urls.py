from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('all_completed_tasks/', views.all_completed_task, name='all_completed_tasks'),
    path('delete_all_tasks/', views.delete_completed_tasks, name='delete_completed_tasks')


]
