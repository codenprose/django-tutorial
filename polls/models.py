import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # class variables are created by instantiating Field Classes and represent a column in a database table
    question_text = models.CharField(max_length=200)  # max_length is used in database schema and validation
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Many-to-One database relationship
    # ForeignKey Docs: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
