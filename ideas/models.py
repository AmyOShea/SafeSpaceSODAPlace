from django.conf import settings
from django.db import models


class Idea(models.Model):
    """
    A model to the board items
    add, save and display chat messages.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    idea_message = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.idea_message


class Board(models.Model):
    """
    A model to open and close
    the idears board.
    """
    id_code = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    items = models.ManyToManyField(Idea)

    def __str__(self):
        return self.id_code



