from django.db import models

# Create your models here.

class Document(models.Model):
    text = models.TextField(null=False)

class words(models.Model):
    word = models.TextField(null=False)
    doc_id = models.ManyToManyField(Document,on_delete=models.CASCADE)