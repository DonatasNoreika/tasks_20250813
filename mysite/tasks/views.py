from django.shortcuts import render
from django.views import generic
from .models import Task

class PostListView(generic.ListView):
    model = Task
    template_name = "tasks.html"
    context_object_name = "tasks"

