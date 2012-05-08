from django.db import models
from corporate.models import Entity
from corpos.models import Corporation

class Player(Entity):
	mail = models.EmailField()
	pc = models.CharField(max_length="15")
	honor = models.PositiveSmallIntegerField()
	citizen = models.ForeignKey(Corporation, null=True, blank=True)