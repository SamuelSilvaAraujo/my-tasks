from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Task, TaskList


def update_task_list_ajax(request):
    if request.is_ajax():
        task_id = request.POST.get('task_id')
        task_list_id = request.POST.get('list_id')

        task = get_object_or_404(Task, pk=task_id)

        task_list = get_object_or_404(TaskList, pk=task_list_id)

        task.task_list = task_list
        task.save()

        data = task.id
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')
