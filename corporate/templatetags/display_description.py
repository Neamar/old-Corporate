# coding=utf8
from django import template
from agents.models import Yakuza, Agency, Fixer
from corpos.models import Corporation

register = template.Library()

@register.simple_tag
def display_description(item):
	if item == 'fixer':
		return "Peu de contacts sont aussi importants pour les corpos que les Fixers &ndash; et, fort heureusement, ceux-ci sont faciles à trouver. Après tout, si les gens ne savent pas les trouver, ils n'ont pas de business. <em>Ergo</em>, voici la liste des fixers de Neo-Tokyo."
	if item == 'yakuza':
		return "Dans la terminologie légale Japonaise, les yakuzas sont connus sous le nom de <em>boryokudan</em>, groupe de violence. Toutefois, les réduire au rôle de gros bras serait une terrible erreur dont certains ne se sont jamais relevés."
	if item == 'agency':
		return "On pourrait attendre des agences gouvernementales une probité sans faille et une fidélité à toute épreuve. S'il n'y a pas grand chose à redire sur ce second point, le premier est plus complexe, et graisser la patte de quelques employés est une nécessité récurrente."
