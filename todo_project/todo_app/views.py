from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Create_Task


# Create your views here.
def addTask(request):
    tasks = request.POST['task']
    Create_Task.objects.create(task=tasks)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Create_Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Create_Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request,pk):
    Create_Task.objects.get(pk=pk).delete()
    return redirect('home')

