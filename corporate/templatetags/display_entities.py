from django import template
from corporate.models import Entity
from agents.models import Yakuza, Fixer, Agency
from corpos.models import Corporation
from joueurs.models import Player

register = template.Library()

def get_fixer_thumbnail(fixer):
	return '<img src="' + fixer.image + '" alt="' + fixer.name + '" class="thumbnail" />'

def get_political_strength(player):
	if player.political_position == 'nc':
		return '&empty;'
	else:
		return str(player.political_strength) + player.political_position[0:3]

@register.inclusion_tag('tags/display_entities.html')
def display_entities(entities):
	# Handle case with only one item
	if isinstance(entities, Entity):
		items = (entities,)
	else:
		items = entities

	# Which attributes should be displayed?
	item_sample = items[0]
	if isinstance(item_sample, (Fixer)):
		attributes = (
			#(get_fixer_thumbnail, 'Img'),
			('capacity_information', 'Inf.'),
			('capacity_datasteal', 'Data.'),
			('capacity_sabotage', 'Sab.'),
			('capacity_scandal', 'Scan.'),
			('capacity_protection', 'Pro.'),
		)
	if isinstance(item_sample, (Yakuza, Agency)):
		attributes = (
			('capacity_information', 'Inf.'),
			('capacity_datasteal', 'Data.'),
			('capacity_sabotage', 'Sab.'),
			('capacity_scandal', 'Scan.'),
			('capacity_protection', 'Pro.'),
		)
	if isinstance(item_sample, (Corporation)):
		attributes = (
			('current_asset', 'Actifs', 'bold'),
			('capacity_information', 'Inf.'),
			('capacity_datasteal', 'Data.'),
			('capacity_sabotage', 'Sab.'),
			('capacity_scandal', 'Scan.'),
		)
		#items = sorted(items, key=lambda corpo: corpo.classement, reverse=True)

	if isinstance(item_sample, (Player)):
		attributes = (
			('pc', 'Joueur'),
			('honor', 'Honneur'),
			('influence', 'Influence'),
			(get_political_strength, 'Politique'),
		)

	# Compute attributes
	displayable_items = []
	for item in items:
		displayable_item = [item]
		for attribute in attributes:
			if callable(attribute[0]):
				attr = attribute[0](item)
			else:
				attr = getattr(item, attribute[0])

			if callable(attr):
				attr = attr()
			if len(attribute) == 3:
				attr = "<strong>" + str(attr) + "</strong>"

			displayable_item.append(attr)
		displayable_items.append(displayable_item)

	return {'items': displayable_items, 'attributes': attributes}
