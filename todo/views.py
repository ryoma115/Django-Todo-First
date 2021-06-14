from django.views import generic
from django.urls import reverse
from .models import Todo


class TodoList(generic.ListView):
  model = Todo
  template_name = 'todo/list.html'
  context_object_name = 'todos'
  ordering = ['limit']

TodoList = TodoList.as_view()

class TodoDetail(generic.DetailView):
  model = Todo
  template_name = 'todo/detail.html'

TodoDetail = TodoDetail.as_view()

class TodoCreate(generic.CreateView):
  model = Todo
  success_url = '/'
  fields = ['title', 'content', 'limit']

TodoCreate = TodoCreate.as_view()

class TodoDelete(generic.DeleteView):
  model = Todo
  success_url = '/'

TodoDelete = TodoDelete.as_view()

class TodoUpdate(generic.UpdateView):
  model = Todo
  template_name = 'todo/update.html'
  fields = ['title', 'content', 'limit']

  # 編集した後、作成物が見える
  def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

TodoUpdate = TodoUpdate.as_view()

