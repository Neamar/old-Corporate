from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Count
from joueurs.models import Player, Share
from corpos.models import Corporation, Asset

def detail(request, slug):
	player = get_object_or_404(Player, slug=slug)
	shares = Share.objects.values('corporation__name').annotate(Count('corporation')).order_by('-corporation__count')
	return render_to_response('joueurs/player_detail.html', {'player': player, 'shares': shares}, context_instance=RequestContext(request))

def shares(request):
	players = Player.objects.all()
	corporations = Corporation.objects.all()

	for player in players:
		shares = []
		for corporation in corporations:
			shares.append(  player.share_set.filter(corporation=corporation).count())
		player.all_shares = shares

	print players[0].all_shares
	return render_to_response('joueurs/shares.html', {'players': players, 'corporations': corporations}, context_instance=RequestContext(request))