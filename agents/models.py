from django.db import models
from corporate.models import AbleEntity

AGENT_STATES = (
	('dead', 'mort'),
	('at_war', 'en guerre'),
	('closed', 'clos'),
)

class Agent(AbleEntity):
	class Meta:
		abstract = True
	friend = models.CharField(max_length="200", null=True, blank=True)
	foe = models.CharField(max_length="200", null=True, blank=True)
	state = models.CharField(max_length="10", null=True, blank=True, choices=AGENT_STATES)

class Fixer(Agent):
	states = ('alive', 'dead')
	def get_state(self):
		if(self.state == ''):
			return states[0]

class Yakuza(Agent):
	def at_war(self):
		return (self.state == 'at_war')

class Agency(Agent):
	pass