from django.shortcuts import render_to_response
from django.template import RequestContext
from agents.models import Fixer, Yakuza, Agency

def index(request):
	fixer_list = Fixer.objects.all()
	yakuza_list = Yakuza.objects.all()
	agency_list = Agency.objects.all()

	return render_to_response('agents/agent_list.html', {'fixer_list': fixer_list,'yakuza_list': yakuza_list,'agency_list': agency_list}, context_instance=RequestContext(request))