from django.db import models

# Create your models here.


class Document(models.Model):
    text = models.TextField(null=False)

    def __str__(self):
        return self.text


class Words(models.Model):
    word = models.TextField(null=False)

    def __str__(self):
        return self.word


class WordFrequencies(models.Model):
    word_id = models.ForeignKey(Words, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    frequency = models.IntegerField()

    class Meta:
        ordering = ['frequency']

    def __str__(self):
        return self.word_id.word + " " + str(self.frequency)
