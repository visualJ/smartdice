from random import randint

from django.db import models


# Create your models here.
class GameSession(models.Model):
    active_user = models.ForeignKey('SessionUser', on_delete=models.SET_NULL, default=None, null=True)


class SessionUser(models.Model):
    name = models.CharField(max_length=200)
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=None)


class RollResult(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=20)
    value = models.IntegerField()
    user = models.ForeignKey(SessionUser, on_delete=models.CASCADE, default=None)
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=None)


class SmartDice(models.Model):
    dice_number = models.IntegerField()
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=None)

    def roll(self):
        return RollResult.objects.create(mode='D6', value=randint(1, 6),
                                         user=self.session.active_user,
                                         session=self.session)
