from django.contrib import admin

from .models import Note

class NoteAdmin(admin.ModelAdmin):
    class meta:
        model = Note

admin.site.register(Note, NoteAdmin)
