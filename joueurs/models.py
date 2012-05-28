# coding=utf-8

from django.db import models
from corporate.models import Entity
from corpos.models import Corporation

PLAYER_POLITICAL_POSITIONS = (
	('nc', 'non aligné'),
	('reformateur', 'réformateur'),
	('nationaliste', 'nationaliste'),
)

class Player(Entity):
	pc = models.CharField(max_length="15")
	honor = models.PositiveSmallIntegerField()
	influence = models.PositiveSmallIntegerField(default=1)
	political_strength = models.PositiveSmallIntegerField(default=0)
	political_position =  models.CharField(max_length=16, choices=PLAYER_POLITICAL_POSITIONS, default='nc')
	citizen = models.ForeignKey(Corporation, null=True, blank=True)
	creation_constraints = models.TextField()

class Share(models.Model):
	player = models.ForeignKey(Player)
	corporation = models.ForeignKey(Corporation)

	def __unicode__(self):
		return self.player.__unicode__() + ' -> ' + self.corporation.__unicode__()