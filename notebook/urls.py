from django.conf.urls import url

from . import views

app_name = 'notebook'

urlpatterns = [
    url(r'^$', views.NoteView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailedNote.as_view(), name='detail'),
    url(r'^add/$', views.AddNote.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditNote.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteNote.as_view(), name='delete'),
]
