import datetime

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, default='MyQuestion')
    date_published = models.DateField(default=datetime.date.today())
    def __str__(self):
        return self.question_text

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default='')
    choice_text = models.CharField(max_length=200, blank=True, null=True)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
