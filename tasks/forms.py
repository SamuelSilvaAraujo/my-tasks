from django import forms

from .models import TaskList, Task


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['title', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da lista'})
        }


class TaskTitleForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da tarefa'})
        }
