from django.db import models
from corporate.models import AbleEntity

class Agent(AbleEntity):
	class Meta:
		abstract = True
	friend = models.CharField(max_length="200", null=True, blank=True)
	foe = models.CharField(max_length="200", null=True, blank=True)

class Fixer(Agent):
	pass

class Yakuza(Agent):
	pass

class Agency(Agent):
	pass