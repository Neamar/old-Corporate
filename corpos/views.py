from django.shortcuts import render_to_response
from django.template import RequestContext
from corpos.models import Corporation, Asset

def bourse(request):
	corporation_list = Corporation.objects.all().order_by('id')
	assets = []
	assets.append(Asset.objects.filter(turn=0).order_by('corporation__id'))
	assets.append(Asset.objects.filter(turn=1).order_by('corporation__id'))
	assets.append(Asset.objects.filter(turn=2).order_by('corporation__id'))
	assets.append(Asset.objects.filter(turn=3).order_by('corporation__id'))
	assets.append(Asset.objects.filter(turn=4).order_by('corporation__id'))
	return render_to_response('corpos/bourse.html', {'corporation_list': corporation_list, 'assets': assets}, context_instance=RequestContext(request))
