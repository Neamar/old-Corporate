from django import template
from django.shortcuts import render_to_response
from django.template.defaultfilters import stringfilter
from django.template.defaultfilters import slugify
from django.conf import settings

import re

register = template.Library()

@register.filter(name='toc')
@stringfilter
def table_of_contents(html, show_toc=None):

	LINK_CLASS = 'anchor'
	TOC_ID = 'table-of-contents'

	re_tags = re.compile('<.*?>', re.DOTALL)
	re_entities = re.compile('&.*?;', re.DOTALL)

	headlines = re.findall('<h(?P<type>\d)>(.*?)<\/h(?P=type)>', html)
	if len(headlines) is 0:
		return html
	last_weight, toc = min([int(x[0]) for x in headlines]), ''
	for h in headlines:
		current_weight = int(h[0])
		s = slugify(h[1])
		html = html.replace('<h%s>%s</h%s>' % (h[0], h[1], h[0]),
							'<h%s><a href="#%s" id="%s" class="%s">%s</a></h%s>' % (current_weight,
												s, s, LINK_CLASS, h[1], current_weight))
		if show_toc is not None:
			if (current_weight-last_weight) >= 1:
				toc = '%s\n\t<ul>\n' % toc[:-6] * (current_weight-last_weight)
			elif (last_weight-current_weight) >= 1:
				toc += '\t</ul>\n\t\t</li>\n'*(last_weight-current_weight)
			toc += '\t\t<li><a href="#%s">%s</a></li>\n' % (s, h[1])
			last_weight = current_weight
	if show_toc is not None:
		toc += '\t</ul>\n'*(toc.count('<ul>') - toc.count('</ul>'))
		toc += '\t\t</li>\n'*(toc.count('<li>') - toc.count('</li>'))
		toc = '<div id="%s">%s\n\t<ul>\n%s\t</ul>\n</div>' % (TOC_ID, show_toc, toc)
	return '%s %s' % (toc, html)