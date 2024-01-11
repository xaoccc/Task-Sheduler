from django.urls import path
from Tasks.tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task', views.create_task, name='create_task'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('complete_task', views.complete_task, name='complete_task'),
]