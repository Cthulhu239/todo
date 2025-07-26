from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect,render



def task_list(request):
    tasks = Task.objects.all()  # gets all tasks from database
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_add(request):
    return HttpResponse("Add a task")

def task_delete(request, id):
    # Your logic to delete the task
    # Example:
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('some-view-name')
