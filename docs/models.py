from django.db import models
from django.template.defaultfilters import slugify

RULE_TYPES = (
	('univers', 'Univers'),
	('regles', 'Regles'),
	('creation', 'Creation'),
	('pratique', 'Pratique'),
)

class Rule(models.Model):
	title = models.CharField(max_length="100")
	slug = models.SlugField(editable=False)
	section = models.CharField(max_length="10", choices=RULE_TYPES)
	content = models.TextField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Rule, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title