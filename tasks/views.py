from django.views.generic import ListView, CreateView
from django.urls import reverse

from .models import TaskList, Task
from .forms import TaskListForm, TaskTitleForm


class TaskListView(ListView):
    template_name = 'task-list/list.html'
    queryset = TaskList.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["task_list_form"] = TaskListForm
        context["task_title_form"] = TaskTitleForm
        return context


class TaskListCreateView(CreateView):
    model = TaskList
    form_class = TaskListForm
    template_name = 'task-list/form.html'

    def get_success_url(self):
        return reverse('task_list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskTitleForm
    template_name = 'task/form.html'

    def form_valid(self, form):
        task_list = TaskList.objects.get(pk=self.kwargs['task_list_pk'])
        form.instance.task_list = task_list
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_list')
