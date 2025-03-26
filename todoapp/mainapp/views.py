from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TaskDb
from django.utils.html import escape, strip_tags

class Home(View):
    def get(self, request):
        tasks = TaskDb.objects.filter(completed=False).order_by('priority')
        return render(request, 'mainapp/home.html', {'tasks':tasks})
    
    def post(self, request):
        title = strip_tags(escape(request.POST.get('title')))
        priority = request.POST.get('priority', 2)

        TaskDb.objects.create(title=title, priority=priority)
        return redirect('home')


def delete_task(request, task_id):
    task = get_object_or_404(TaskDb, id=task_id)
    task.delete()
    return redirect('home')


def edit_task(request, task_id):
    task = get_object_or_404(TaskDb, id=task_id)
    new_task = ''
    if request.method == 'POST':
        new_task = strip_tags(escape(request.POST.get('title_edit')))
        new_priority = request.POST.get('priority', 2)

    if new_task:
        task.title = new_task
        task.priority = new_priority
        task.save()
        return redirect('home')
    
    return render(request, 'mainapp/edit_task.html', {'task':task})



def complete_task(request, task_id):
    task = get_object_or_404(TaskDb, id=task_id)

    # Update the task status to completed
    task.completed = True
    task.save()
    return redirect('home')



def complete_task(request, task_id):
    task = get_object_or_404(TaskDb, id=task_id)

    # Update the task status to completed
    task.completed = True
    task.save()
    return redirect('home')

def all_completed_task(request):
    tasks = TaskDb.objects.filter(completed=True)
    return render(request, 'mainapp/completed_tasks.html', {'tasks':tasks})



def delete_completed_tasks(request):
    TaskDb.objects.filter(completed=True).delete()
    return redirect('all_completed_tasks')
