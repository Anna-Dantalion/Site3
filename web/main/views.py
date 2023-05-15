from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def parents(request):
    return render(request, 'main/parents.html')

def students(request):
    return render(request, 'main/students.html')
