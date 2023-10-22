from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>To-DO Project</h1>")
    return render(request,'home.html')