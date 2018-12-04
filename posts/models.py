from django.db import models
from datetime import datetime
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
 
class PostCassandra(Model):
    id = columns.Integer(primary_key=True)
    title = columns.Text(required=False)
    body = columns.Text(required=False)
    created_at = columns.DateTime(required=False, default=datetime.now)

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
