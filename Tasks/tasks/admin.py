from django.contrib import admin
from Tasks.tasks.models import Task


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "is_completed"]
    list_filter = ["is_completed"]
    search_fields = ["name", "description"]
