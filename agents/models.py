from django.db import models
from corporate.models import AbleEntity
from joueurs.models import Player

AGENT_STATES = (
	('dead', 'mort'),
	('at_war', 'en guerre'),
	('vanished', 'disparu'),
	('closed', 'clos'),
)

YAKUZA_FOSTER_TYPES = (
	('kobun', 'obun'),
	('oyabun', 'oyabun'),
)

class Agent(AbleEntity):
	class Meta:
		abstract = True
	friend = models.CharField(max_length="200", null=True, blank=True)
	private_friend = models.CharField(max_length="200", null=True, blank=True)
	foe = models.CharField(max_length="200", null=True, blank=True)
	private_foe = models.CharField(max_length="200", null=True, blank=True)
	loyalties = models.TextField(null=True, blank=True)
	state = models.CharField(max_length="10", null=True, blank=True, choices=AGENT_STATES)

class Fixer(Agent):
	states = ('alive', 'dead')
	image = models.CharField(max_length="50")

	def get_state(self):
		if(self.state == ''):
			return states[0]

class Yakuza(Agent):
	def at_war(self):
		return (self.state == 'at_war')

class Agency(Agent):
	political_side = models.CharField(max_length="20")
	political_description = models.TextField()

class CROC(Agent):
	player = models.ForeignKey(Player)
	level = models.PositiveSmallIntegerField()