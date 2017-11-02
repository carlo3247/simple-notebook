from .models import Note
from django import forms

class SearchForm(forms.Form):
    search_title =  forms.CharField(
                    required = False,
                    label='Titlesearch: ',
                    widget=forms.TextInput(attrs={'placeholder': 'any title'}))

    search_text =  forms.CharField(
                    required = False,
                    label='Textsearch: ',
                    widget=forms.TextInput(attrs={'placeholder': 'any text'}))
