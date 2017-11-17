from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^session/$', views.session, name='session'),
    url(r'^session/(?P<session_id>\d*)$', views.session, name='session'),
    url(r'^endsession$', views.end_session, name='endsession'),
    url(r'^newsession$', views.new_session, name='newsession'),
    url(r'^adduser', views.add_user, name='adduser'),
    url(r'^removeuser', views.remove_user, name='removeuser'),
]
