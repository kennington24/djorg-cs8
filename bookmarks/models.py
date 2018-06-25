from django.db import models
from uuid import uuid4

class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=200)
  url = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)