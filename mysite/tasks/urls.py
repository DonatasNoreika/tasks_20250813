from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("tasks/", PostListView.as_view(), name="tasks"),
    path("tasks/<int:pk>", PostDetailView.as_view(), name="task"),
    path("tasks/create", PostCreateView.as_view(), name="task_create"),
]
