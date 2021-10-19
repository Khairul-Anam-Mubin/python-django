from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        #print (title , description)
        if title != "":
            ins = Task(taskTitle = title, taskDescription= description)
            ins.save()
            context = {'success': True}
    return render(request , 'index.html' , context)

def tasks(request):
    alltask = Task.objects.all()
    context = {'tasks':alltask}
    return render(request , 'tasks.html',context)