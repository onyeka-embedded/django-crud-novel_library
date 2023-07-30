from django.db import models
import uuid

# Create your models here.
class Novel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=2000, blank=True)
    author = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(blank=False, default=2000)
    novel_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return self.title + ' | ' + str(self.author) + ' | ' + str(self.year)
    
