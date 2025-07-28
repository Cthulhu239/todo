from django.http import HttpResponse
from .models import Task
from django.shortcuts import  redirect, get_object_or_404,render



def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')

    tasks = Task.objects.all().order_by('-created')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed') == 'on'

        if title:
            task.title = title
            task.completed = completed
            task.save()
        return redirect('task_list')

    # GET request: Show the edit form inline for this task
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks, 'editing_task': task})
 

def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('task_list')          




      


