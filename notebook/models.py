from django.db import models
from django.urls import reverse

class Notebook(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('notebook:home')

class Note(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('notebook:detail', kwargs={'pk': self.pk, 'note_id': self.id})
