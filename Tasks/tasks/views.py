from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Tasks.tasks.forms import CreateTaskForm
from Tasks.tasks.models import Task


# Create your views here.
def index(request):
    title_filter = request.GET.get("title_filter", "")
    contents_filter = request.GET.get("contents_filter", "")
    completed_filter = request.GET.get("completed_filter", "")
    all_tasks = Task.objects.all()

    if completed_filter == "Yes":
        all_tasks = all_tasks.filter(is_completed=True)

    if completed_filter == "No":
        all_tasks = all_tasks.filter(is_completed=False)

    if title_filter:
        all_tasks = all_tasks.filter(name__icontains=title_filter.lower())

    if contents_filter:
        all_tasks = all_tasks.filter(description__icontains=contents_filter.lower())


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
        'tasks': all_tasks,
        'title_filter': title_filter,
        'contents_filter': contents_filter,
        'completed_filter': completed_filter,
        'form': form
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

    return render(request, 'index.html', context)

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

