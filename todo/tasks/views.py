from django.shortcuts import render


from .models import Task

from . forms import TaskForm
# Create your views here.

def index(request):

    form = TaskForm()

    tasks = Task.objects.all()

    context = {'tasks': tasks,
               'TaskForm': form}

    return render(request, 'tasks/tasks.html', context=context)



