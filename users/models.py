from django.db import models

# Create your models here.
from django.db import models 

class TestMode(models.Model):
    userId = models.IntegerField(null=True)
    title = models.CharField(max_length=2000,null=True)
    body = models.TextField(max_length=2000,null=True)
    jsondata = models.JSONField(null=True)

    def __str__(self):
        return self.title

class FileUpload(models.Model):
    name = models.CharField(max_length=200)
    upload = models.FileField()

    def __str__(self):
        return self.name
