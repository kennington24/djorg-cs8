from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=200)
  url = models.TextField(max_length=200)
  created_at = models.DateTimeField

class PersonalBookmark(Bookmark):
  user = models.ForeignKey(User, on_delete=models.CASCADE)