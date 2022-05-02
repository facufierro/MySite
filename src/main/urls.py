from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("create_todo_list/", views.create_todo_list, name="create_todo_list"),
    path("view/", views.view, name="view"),
]
