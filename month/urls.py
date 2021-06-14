from django.urls import path
from . import views

app_name = 'month'

urlpatterns = [
  path('month/', views.MonthCalendar.as_view(), name='month'),
  path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
]

