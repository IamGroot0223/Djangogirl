from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):    #对象的描述
        return self.question_text

    def was_published_recently(self):
        return self.pub_date


class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


