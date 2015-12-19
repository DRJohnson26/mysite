from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.



class Question(models.Model):
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
