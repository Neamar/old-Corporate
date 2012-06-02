from django import template
from django.template.defaultfilters import stringfilter
from django.template.defaultfilters import slugify
import re

register = template.Library()

@register.filter(name='cf')
@stringfilter
def link_cf(html):
	def cfify(matches):
		if matches.group(1) == "mep/":
			return "(cf. <a href=\"/docs/mise-en-place#" + slugify(matches.group(2)) + "\">" + matches.group(2) + "</a>)"
		else:
			return "(cf. <a href=\"/docs/regles#" + slugify(matches.group(2)) + "\">" + matches.group(2) + "</a>)"

	html = re.sub(r'\(cf\. (mep/)?(.+?)\)', cfify, html)
	return html