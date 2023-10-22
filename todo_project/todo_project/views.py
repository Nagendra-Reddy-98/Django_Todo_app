from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import Create_Task


def home(request):
    # return HttpResponse("<h1>To-DO Project</h1>")
    tasks = Create_Task.objects.filter(is_completed=False).order_by('updated_at')
    done_tasks = Create_Task.objects.filter(is_completed=True)
    return render(request, 'home.html', context={'tasks': tasks, 'done_tasks': done_tasks})
