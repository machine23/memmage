from django.db import models
from django.contrib.auth.models import User


class QuestionList(models.Model):
    name = models.CharField(maxlength=100)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    question_list = models.ForeingKey(QuestionList, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
