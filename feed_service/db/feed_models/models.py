from datetime import datetime

from django.db import models


# Create your models here.

class Question(models.Model):
    question_string = models.CharField(max_length=1024)
    user_id = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=datetime.now())


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user_id = models.CharField(max_length=256)
    answer_string = models.CharField(max_length=1024)
    created_date = models.DateTimeField(default=datetime.now())


class Upvote(models.Model):
    answer = models.ForeignKey(Answer)
    user_id = models.CharField(max_length=256)


class Downvote(models.Model):
    answer = models.ForeignKey(Answer)
    user_id = models.CharField(max_length=256)


class Notification(models.Model):
    entity_choice = (("Answer", "Answer"),
                     ("Upvote", "Upvote"),
                     ("Downvote", "Downvote"))

    entity_type = models.CharField(max_length=56, choices = entity_choice, default = None)
    entity_id = models.IntegerField()
    action_by = models.CharField(max_length=64)
    owner_id = models.CharField(max_length=64)
    is_read = models.BooleanField(default=False)
