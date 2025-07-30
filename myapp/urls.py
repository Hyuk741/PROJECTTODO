from django.urls import path

from myapp.cb_views import TodoListView, TodoCreateView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path('todo/', TodoListView.as_view(), name='cbv_todo_list'),
    path('todo/create/', TodoCreateView.as_view(), name='cbv_todo_create'),
    path('todo/<int:pk>/', TodoDeleteView.as_view(), name='cbv_todo_info'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),
    ]