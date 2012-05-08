from django import template
from corporate.models import Entity
from agents.models import Yakuza, Fixer, Agency
from corpos.models import Corporation
from joueurs.models import Player

register = template.Library()

@register.inclusion_tag('tags/display_entities.html')
def display_entities(entities):
	# Handle case with only one item
	if isinstance(entities, Entity):
		items = (entities,)
	else:
		items = entities

	# Which attributes should be displayed?
	item_sample = items[0]
	if isinstance(item_sample, (Yakuza, Agency, Fixer)):
		attributes = (
			('capacity_information', 'Inf.'),
			('capacity_datasteal', 'Data.'),
			('capacity_sabotage', 'Sab.'),
			('capacity_scandal', 'Scan.'),
			('capacity_protection', 'Pro.'),
		)
	if isinstance(item_sample, (Corporation)):
		attributes = (
			('capacity_information', 'Inf.'),
			('capacity_datasteal', 'Data.'),
			('capacity_sabotage', 'Sab.'),
			('capacity_scandal', 'Scan.'),
		)

	if isinstance(item_sample, (Player)):
		attributes = (
			('pc', 'Joueur'),
			('honor', 'Honneur'),
			('citizen', 'Citoyen'),
		)

	# Compute attributes
	displayable_items = []
	for item in items:
		displayable_item = [item]
		for attribute in attributes:
			displayable_item.append(getattr(item, attribute[0]))
		displayable_items.append(displayable_item)

	return {'items': displayable_items, 'attributes': attributes}