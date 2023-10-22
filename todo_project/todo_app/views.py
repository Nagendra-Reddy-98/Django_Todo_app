from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Create_Task

# Create your views here.
def addTask(request):
    tasks=request.POST['task']
    Create_Task.objects.create(task=tasks)
    return redirect('home')
