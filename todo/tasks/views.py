from django.shortcuts import render, redirect


from .models import Task

from . forms import TaskForm
# Create your views here.

def index(request):

    form = TaskForm()

    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context = {'tasks': tasks,
               'TaskForm': form}

    return render(request, 'tasks/tasks.html', context=context)



def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {'TaskForm': form}

    return render(request, 'tasks/update-task.html', context=context)



def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.METHOD == 'POST':
        task.delete()
        return redirect('/')
    context = {'task':task}

    return render(request, 'tasks/delete-task.html', context=context)






