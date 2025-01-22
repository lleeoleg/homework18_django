from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'index.html'
    
class CreateTodo(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')
    
class UpdateTodo(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'todo_id'
    
class ListTodo(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todos'
    
class DetailTodo(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'todo'
    pk_url_kwarg = 'todo_id'

class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('index')