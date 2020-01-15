from django.db import models
from simple_history.models import HistoricalRecords
from enum import Enum
from django_enum_choices.fields import EnumChoiceField
from django.contrib.auth.models import User

# Create your models here.

# Enum-class for status in post Model
class enum_status(Enum):
    draft = 'draft'
    unpublished = 'unpublished'
    published = 'published'

# Model for post table
class post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    status =  EnumChoiceField(enum_status)
    retrieves_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    history = HistoricalRecords()

