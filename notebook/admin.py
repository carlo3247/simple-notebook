from django.contrib import admin

from .models import Note, Notebook

class NoteAdmin(admin.ModelAdmin):
    class meta:
        model = Note

class NotebookAdmin(admin.ModelAdmin):
    class meta:
        model = Notebook

admin.site.register(Note, NoteAdmin)
admin.site.register(Notebook, NoteAdmin)
