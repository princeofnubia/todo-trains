from django.urls import path
from . import views

urlpatterns = [
    path('getTodos/', views.getTodos, name="getTodos"), # get the todos a user
    path('updateTodo/', views.updateTodo, name="updateTodo"), # call it when we are editing
    path('trashTodo/', views.trash, name="trashTodos"), # handles the soft deletion of the todo
    path('emptyTrash/', views.emptyTrash, name="emptyTrash"), # completely delete it from your system
    path('archiveTodo/', views.archiveTodo, name="archiveTodo"), # archived todo
    path("getTrash/", views.getTrash, name="getTrash"), # get todos that are trashed
    path("getArchive/", views.getArchived, name="getArchived"), # get todos that are archived
    path("createTodo/", views.createTodo, name="createTodo")

]