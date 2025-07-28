from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from myapp.forms import TodoForm, TodoUpdateForm
from myapp.models import Todo
from django.urls import reverse

@login_required()
def todo_list(request):
    todo_list = Todo.objects.filter(user=request.user).order_by('created_at')
    q = request.GET.get('q')
    if q:
        todo_list = todo_list.filter(Q(title__icontains=q)| Q(description_icontains=q))

    paginator = Paginator(todo_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    todos = [
        {'title': '공부하기', 'completed': False},
        {'title': '운동하기', 'completed': True},
    ]
    context = {
        'todo': todos
    }
    return render(request, 'todo_list.html', context)

@login_required()
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    context = {
        'form': form
    }
    return render(request, 'todo_create.html', context)
@login_required()
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    context = {
        'todo': todo.__dict__
    }
    return render(request, 'todo_info.html', context)

@login_required()
def todo_update(request):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    context = {
        'form': form
    }
    return render(request, 'todo_update.html', context)


@login_required()
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect(reverse('todo_list'))


def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo_detail.html', {'todo': todo})

