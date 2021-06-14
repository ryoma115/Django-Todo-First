from django.db import models
from django.utils import timezone
from django.urls import reverse

class Todo(models.Model):
  title: str = models.CharField(
    max_length=100 
  )
  content = models.TextField()
  limit = models.DateField(
    default= timezone.now() + timezone.timedelta(days=1),
    blank=True
  )
  def __str__(self) -> str:
      return self.title
    