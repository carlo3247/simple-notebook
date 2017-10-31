from django.db import models
from django.urls import reverse

class Note(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('notebook:detail', kwargs={'pk': self.pk})
