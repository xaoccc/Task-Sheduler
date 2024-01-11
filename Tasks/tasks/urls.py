from django.urls import path
from Tasks.tasks import views

urlpatterns = [
    path('', views.index, name='index'),
]