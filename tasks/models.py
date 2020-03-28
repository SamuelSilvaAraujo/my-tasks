from django.db import models


class TaskList(models.Model):
    title = models.CharField('Título da Lista', max_length=50)


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    title = models.CharField('Título da Tarefa', max_length=50)
    description = models.TextField('Descrição da Tarefa', null=True, blank=True)
    creating_date = models.DateField(auto_now_add=True)
    conclusion_date = models.DateField('Data de Entrega', null=True, blank=True)


class TaskAttachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_attachment')
