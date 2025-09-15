from django.shortcuts import render


from .models import Task
# Create your views here.

def index(request):

    tasks = Task.objects.all()

    context = {'tasks': tasks}

    return render(request, 'tasks/tasks.html', context=tasks)



