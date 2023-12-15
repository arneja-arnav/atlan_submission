from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True)

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    options = models.JSONField(blank=True, default=list)
    metadata = models.JSONField(blank=True)

class Response(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    metadata = models.JSONField(blank=True)

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    metadata = models.JSONField(blank=True)
