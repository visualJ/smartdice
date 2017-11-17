from django.db import models


# Create your models here.
class GameSession(models.Model):
    pass


class SessionUser(models.Model):
    name = models.CharField(max_length=200)
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=None)
