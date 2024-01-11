from django import forms
from Tasks.tasks.models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']





