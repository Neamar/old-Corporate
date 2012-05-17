# coding=utf8
from django import template
from agents.models import Agent, Agency
from corpos.models import Corporation
from joueurs.models import Player

register = template.Library()

@register.simple_tag
def entity_link(item):
	if isinstance(item, Agent):
		return '<a href="/agents/#' + item.slug + '" title="' + item.get_capacity_display() + '">' + item.__unicode__() + '</a>'
	if isinstance(item, Corporation):
		return '<a href="/corpos/#' + item.slug + '" title="' + item.get_capacity_display() + '">' + item.__unicode__() + '</a>'
	if isinstance(item, Player):
		return '<a href="/joueurs/#' + item.slug + '">' + item.__unicode__() + '</a>'
	#Does not seems to be linkable.
	return item