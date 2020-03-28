from django.urls import path, include

from .views import *
from .ajax import update_task_list_ajax

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task-list/', include([
        path('create/', TaskListCreateView.as_view(), name='task_list_create'),
        path('<int:task_list_pk>/', include([
            path('task/', include([
                path('create/', TaskCreateView.as_view(), name='task_create')
            ])),
        ])),
    ])),

    path('update/task/list/', update_task_list_ajax, name='update_task_list_ajax')
]
