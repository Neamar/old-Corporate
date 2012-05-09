from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Count
from joueurs.models import Player, Share

def detail(request, slug):
	player = get_object_or_404(Player, slug=slug)
	shares = Share.objects.values('corporation__name').annotate(Count('corporation')).order_by('-corporation__count')
	return render_to_response('joueurs/player_detail.html', {'player': player, 'shares': shares}, context_instance=RequestContext(request))