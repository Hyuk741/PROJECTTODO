from django.shortcuts import render, get_object_or_404

from myapp.models import Todo


def todo_list(request):
    todos = [
        {'title': '공부하기', 'completed': False},
        {'title': '운동하기', 'completed': True},
    ]
    context = {
        'todo': todos
    }
    return render(request, 'todo_list.html', context)

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo_detail.html', {'todo': todo})

