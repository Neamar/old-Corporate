from django.db import models
from corporate.models import AbleEntity

CORPORATION_POLITICAL_POSITIONS = (
	('nc', 'non pertinent'),
	('reformateur', 'reformateur'),
	('nationaliste', 'nationaliste'),
)

CORPORATION_RANKS = (
	('AA', 'AA'),
	('AAA', 'AAA'),
)

CORPORATION_ORIGINS = (
	('japanocorp', 'japanocorp'),
	('gaijin', 'gaijin'),
	('japanogaijin', 'japanocorp-gaijin'),
)

class Corporation(AbleEntity):
	political_position = models.CharField(max_length=16, choices=CORPORATION_POLITICAL_POSITIONS)
	origin = models.CharField(max_length="12", choices=CORPORATION_ORIGINS)
	rank = models.CharField(max_length="3", choices=CORPORATION_RANKS)
	on_first = models.TextField()
	on_first_effect = models.TextField()
	on_last = models.TextField()
	on_last_effect = models.TextField()
	on_crash = models.TextField()
	on_crash_effect = models.TextField()

	def get_capacity_display(self):
		return "i%s / d%s / s%s / t%s" % (self.capacity_information, self.capacity_datasteal, self.capacity_sabotage, self.capacity_scandal)

	def current_asset(self):
		return self.asset_set.order_by('-turn')[0].value

class Asset(models.Model):
	turn = models.PositiveSmallIntegerField()
	corporation = models.ForeignKey(Corporation)
	value = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return 'Assets for ' + self.corporation.slug + ' at ' + str(self.turn) + ' (' + str(self.value) + ')'