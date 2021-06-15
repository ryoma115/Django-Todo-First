import calendar
from collections import deque
import datetime
from month import models
from todo.models import Todo

class BaseCalendarMixin:
  first_weekday = 0
  week_names = ['月', '火', '水', '木', '金', '土', '日']

  def setup_calendar(self):

    self._calendar = calendar.Calendar(self.first_weekday)

  def get_week_names(self):
    week_names = deque(self.week_names)
    week_names.rotate(-self.first_weekday)
    return week_names


class MonthCalendarMixin(BaseCalendarMixin):
  def get_previous_month(self, date):
    if date.month == 1:
      return date.replace(year=date.year-1, month=12, day=1)
    else:
      return date.replace(month=date.month-1, day=1)

  def get_next_month(self, date):
    if date.month == 12:
      return date.replace(year=date.year+1, month=1, day=1)
    else:
      return date.replace(month=date.month+1, day=1)

  def get_month_days(self, date):
    return self._calendar.monthdatescalendar(date.year, date.month)

  def get_month_days_with_todo(self):
    month_days_with_todo = []
    current_month = self.get_current_month()
    todos = Todo.objects.all()
    """
    month_days_with_todo = [
      [{day:1/1,todo:Todo},{}],
      []
    ]
    """
    for week in self.get_month_days(current_month):
      month_days_with_todo.append([])
      for day in week:
        month_days_with_todo[-1].append({"date":day})
        for todo in todos:
          if day == todo.limit:
            month_days_with_todo[-1][-1]["todo"] = todo
      print(month_days_with_todo)
    return month_days_with_todo
  
  def get_current_month(self):
    month = self.kwargs.get('month')
    year = self.kwargs.get('year')
    if month and year:
      month = datetime.date(year=int(year), month=int(month), day=1)
    else:
      month = datetime.date.today().replace(day=1)
    return month

  def get_month_calendar(self):
    self.setup_calendar()
    current_month = self.get_current_month()
    

    calendar_data = {
      'now': datetime.date.today(),
      # 'month_days': self.get_month_days(current_month),
      'month_days_with_todo': self.get_month_days_with_todo(),
      'month_current': current_month,
      'month_previous': self.get_previous_month(current_month),
      'month_next': self.get_next_month(current_month),
      'week_names': self.get_week_names(),
    }
    return calendar_data