from random import randint, choice

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
    value = models.CharField(max_length=200)
    user = models.ForeignKey(SessionUser, on_delete=models.CASCADE, default=None)
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=None)


class SmartDice(models.Model):
    dice_number = models.IntegerField()
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=None)
    mode = models.CharField(max_length=20, default='D6')

    modes = {'D6': lambda dice: randint(1, 6),
             'D12': lambda dice: randint(1, 12),
             'D20': lambda dice: randint(1, 20),
             'user': lambda dice: choice(dice.session.sessionuser_set.all()).name}

    def roll(self):
        roll_value = self.modes[self.mode](self)
        return RollResult.objects.create(mode=self.mode, value=roll_value,
                                         user=self.session.active_user,
                                         session=self.session)

    def set_mode(self, new_mode):
        if new_mode in SmartDice.modes.keys():
            self.mode = new_mode
            self.save()
