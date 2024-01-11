from django.shortcuts import render, redirect

# from Tasks.tasks.forms import
from Tasks.tasks.models import Task


# Create your views here.
def index(request):
    all_tasks = Task.objects.all()

    context = {
        'tasks': all_tasks
    }

    return render(request, 'index.html', context)

