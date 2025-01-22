from django.urls import path
from .views import Index, CreateTodo, UpdateTodo, ListTodo, DetailTodo, DeleteTodo

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', CreateTodo.as_view(), name='create'),
    path('update/<int:todo_id>', UpdateTodo.as_view(), name='update'),
    path('list/', ListTodo.as_view(), name='list'),
    path('detail/<int:todo_id>', DetailTodo.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete')
]
