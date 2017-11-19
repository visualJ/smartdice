from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^session/newsession$', views.new_session, name='newsession'),
    url(r'^session/$', views.session, name='session'),
    url(r'^session/(?P<session_id>\d*)$', views.session, name='session'),
    url(r'^session/(?P<session_id>\d*)/endsession', views.end_session, name='endsession'),
    url(r'^session/(?P<session_id>\d*)/adduser$', views.add_user, name='adduser'),
    url(r'^session/(?P<session_id>\d*)/removeuser/(?P<user_id>\d*)$', views.remove_user, name='removeuser'),
    url(r'^session/(?P<session_id>\d*)/activateuser/(?P<user_id>\d*)$', views.activate_user, name='activateuser'),
    url(r'^session/(?P<session_id>\d*)/adddice$', views.add_dice, name='adddice'),
    url(r'^session/(?P<session_id>\d*)/removedice/(?P<dice_id>\d*)$', views.remove_dice, name='removedice'),
]
