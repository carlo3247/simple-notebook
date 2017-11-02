from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'notebook'

urlpatterns = [

    url(r'^$', login_required(views.NotebookView.as_view()), name='home'),
    url(r'^add-notebook/$', login_required(views.AddNotebook.as_view()), name='add-notebook'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.NoteView.as_view()), name='all-notes'),
    url(r'^(?P<pk>[0-9]+)/delete$', login_required(views.DeleteNotebook.as_view()), name='delete-notebook'),
    url(r'^(?P<pk>[0-9]+)/add-note/$', login_required(views.AddNote.as_view()), name='add-note'),
    url(r'^(?P<pk>[0-9]+)/detail/(?P<id>[0-9]+)$', login_required(views.DetailedNote.as_view()), name='detail-note'),
    url(r'^(?P<pk>[0-9]+)/edit/(?P<id>[0-9]+)$', login_required(views.EditNote.as_view()), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/(?P<id>[0-9]+)$', login_required(views.DeleteNote.as_view()), name='delete'),
    url(r'Search/$', login_required(views.Search.as_view()), name='searcher'),
]
