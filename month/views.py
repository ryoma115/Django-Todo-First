from calendar import calendar
from django.views import generic
from . import mixins

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
  template_name = 'month/month.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    calendar_context = self.get_month_calendar()
    context.update(calendar_context)
    return context
