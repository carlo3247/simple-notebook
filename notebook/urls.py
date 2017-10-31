from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'notebook'

urlpatterns = [

    url(r'^$', login_required(views.NoteView.as_view()), name='home'),
    # url(r'^$', views.NoteView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/detail/$', login_required(views.DetailedNote.as_view()), name='detail'),
    url(r'^add/$', login_required(views.AddNote.as_view()), name='add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', login_required(views.EditNote.as_view()), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', login_required(views.DeleteNote.as_view()), name='delete'),
]
