from calendar import calendar
from django.views import generic
from . import mixins
from todo.models import Todo

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
  template_name = 'month/month.html'


  def get_context_data(self, **kwargs):
    # todos = Todo.objects.all()
    todo = Todo.objects.get(pk=2)

    title = todo.title
    # for todo in todos:
    #   print(todo.title)
    #   print(todo.content)
    #   print(todo.limit)
    
    context = super().get_context_data(**kwargs)
    calendar_context = self.get_month_calendar()
    context.update(calendar_context)
    return context
