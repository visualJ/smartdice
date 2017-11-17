from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from webapp.models import GameSession, SessionUser


def index(request):
    return render(request, 'webapp/index.html', {'sessions': list(map(lambda x: x.id, GameSession.objects.all()))})


def show_session(request, game_session):
    context = {'game_session': game_session,
               'session_url': request.build_absolute_uri(reverse('session', args=[game_session.id]))}
    return render(request, 'webapp/session.html', context)


def session(request, session_id=None):
    session_id = session_id if session_id else request.POST.get('sessionid', 0)
    game_session = get_object_or_404(GameSession, id=session_id)
    return show_session(request, game_session)


def new_session(request):
    game_session = GameSession()
    game_session.save()
    return show_session(request, game_session)


def end_session(request):
    session_id = request.POST.get('sessionid', 0)
    game_session = get_object_or_404(GameSession, id=session_id)
    game_session.delete()
    return redirect('index')


def add_user(request):
    session_id = request.POST.get('sessionid', 0)
    game_session = get_object_or_404(GameSession, id=session_id)
    user_name = request.POST.get('username', '')
    session_user = SessionUser(name=user_name, session=game_session)
    session_user.save()
    return redirect('session', session_id=session_id)


def remove_user(request):
    session_id = request.POST.get('sessionid', 0)
    user_id = request.POST.get('userid', 0)
    session_user = get_object_or_404(SessionUser, id=user_id)
    session_user.delete()
    return redirect('session', session_id=session_id)
