from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from webapp.models import GameSession, SessionUser, SmartDice


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


def end_session(request, session_id):
    game_session = get_object_or_404(GameSession, id=session_id)
    game_session.delete()
    return redirect('index')


def add_user(request, session_id):
    game_session = get_object_or_404(GameSession, id=session_id)
    user_name = request.POST.get('username', '')
    session_user = SessionUser(name=user_name, session=game_session)
    session_user.save()

    # make the user active, if it is the first user in the session
    if not game_session.active_user:
        game_session.active_user = session_user
        game_session.save()
    return redirect('session', session_id=session_id)


def remove_user(request, session_id, user_id):
    game_session = get_object_or_404(GameSession, id=session_id)
    session_user = get_object_or_404(SessionUser, id=user_id)
    session_user.delete()

    # make the next user active, if the session is not empty
    if game_session.sessionuser_set.count() > 0:
        game_session.active_user = game_session.sessionuser_set.first()
        game_session.save()
    return redirect('session', session_id=session_id)


def activate_user(request, session_id, user_id):
    game_session = get_object_or_404(GameSession, id=session_id)
    session_user = get_object_or_404(SessionUser, id=user_id)
    game_session.active_user = session_user
    game_session.save()
    return redirect('session', session_id=session_id)


def add_dice(request, session_id):
    dice_number = request.POST.get('dice_number', 0)
    game_session = get_object_or_404(GameSession, id=session_id)
    new_dice = SmartDice(dice_number=dice_number, session=game_session)
    new_dice.save()
    return redirect('session', session_id=session_id)


def remove_dice(request, session_id, dice_id):
    game_session = get_object_or_404(GameSession, id=session_id)
    dice = get_object_or_404(SmartDice, id=dice_id)
    dice.delete()
    return redirect('session', session_id=session_id)
