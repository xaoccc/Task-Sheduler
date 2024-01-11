from django.http import HttpResponse
from django.shortcuts import render, redirect

from Tasks.tasks.forms import CreateTaskForm
from Tasks.tasks.models import Task


# Create your views here.
def index(request):
    all_tasks = Task.objects.all()

    context = {
        'tasks': all_tasks
    }

    return render(request, 'index.html', context)


def create_task(request):

    if request.method == "GET":
        form = CreateTaskForm()

    else:
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            Task.objects.create(name=name, description=description, is_completed=False)
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'new_task.html', context)

def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')

        try:
            task_to_delete = Task.objects.get(id=task_id)
            task_to_delete.delete()
            return redirect('index')
        except Task.DoesNotExist:
            return HttpResponse("Task not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=400)

def complete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')

        try:
            task_to_delete = Task.objects.get(id=task_id)
            task_to_delete.is_completed = True
            task_to_delete.save()
            return redirect('index')
        except Task.DoesNotExist:
            return HttpResponse("Task not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=400)

