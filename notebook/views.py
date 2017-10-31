from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy

from django.http import HttpResponse

from .models import Note

class NoteView(generic.ListView):
    template_name = 'notebook/note.html'

    context_object_name = 'note_book'

    def get_queryset(self):
        return Note.objects.all()

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

def add(request):
    return HttpResponse("hello")
