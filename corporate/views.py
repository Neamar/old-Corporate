from agents.models import Fixer, Yakuza, Agency
from joueurs.models import Player
from corpos.models import Corporation
from django.shortcuts import render_to_response
from django.template import RequestContext

def recap(request):
	fixer_list = Fixer.objects.all()
	yakuza_list = Yakuza.objects.all()
	agency_list = Agency.objects.all()
	corporation_list = Corporation.objects.all()
	player_list = Player.objects.all()

	return render_to_response('recap.html',
							  {'fixer_list': fixer_list,
							   'yakuza_list': yakuza_list,
							   'agency_list': agency_list,
							   'corporation_list': corporation_list,
							   'player_list': player_list,
							   }
							  , context_instance=RequestContext(request))