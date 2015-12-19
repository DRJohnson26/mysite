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
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
