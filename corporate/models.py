from django.db import models
from django.template.defaultfilters import slugify

class Entity(models.Model):
	class Meta:
		abstract = True

	name = models.CharField(max_length="100")
	slug = models.SlugField(editable=False)
	type = models.SlugField(editable=False)
	description = models.TextField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
			self.type = self.__class__.__name__.lower();
		super(Entity, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class AbleEntity(Entity):
	class Meta:
		abstract = True

	capacity_information = models.PositiveSmallIntegerField()
	capacity_datasteal = models.PositiveSmallIntegerField()
	capacity_sabotage = models.PositiveSmallIntegerField()
	capacity_scandal = models.PositiveSmallIntegerField()
	capacity_protection = models.PositiveSmallIntegerField()