from django.urls import path
from Tasks.tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('complete_task', views.complete_task, name='complete_task'),
]