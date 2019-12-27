from django.db import models

# Create your models here.
from django.conf import settings
from django.db  import models
from django.utils import timezone


class Post(models.Model):
    author  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title   = models.CharField(max_length=100)
    text    = models.TextField()
    createdDate = models.DateField()
    publishedDate = models.DateField()

    def publish(self):
        self.publishedDate = timezone.now()
    def __str__(self):
        return  self.title