from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy

from django.http import HttpResponse

from .models import Note, Notebook

class NotebookView(generic.ListView):
    template_name = 'notebook/overview.html'

    context_object_name = 'note_books'

    def get_queryset(self):
        return Notebook.objects.all()

class NoteView(generic.ListView):
    template_name = 'notebook/note.html'

    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(notebook__exact=1)

class DetailedNote(generic.DetailView):
    model = Note

    template_name = 'notebook/details.html'

    def get_queryset(self):
        return Note.objects.filter(created__lte=timezone.now())

class AddNote(generic.edit.CreateView):

    model = Note
    fields = ['title', 'text']

class EditNote(generic.edit.UpdateView):

    model = Note
    fields = ['title', 'text']

class DeleteNote(generic.edit.DeleteView):

    model = Note
    success_url = reverse_lazy('notebook:home')


class AddNotebook(generic.edit.CreateView):

    model = Notebook
    fields = ['name']

class DeleteNotebook(generic.edit.DeleteView):

    model = Notebook
    success_url = reverse_lazy('notebook:home')
