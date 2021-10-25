from django.contrib import admin
from app.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(Task, TaskAdmin)