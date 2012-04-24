from django.shortcuts import render_to_response, get_object_or_404
from doc.models import Rule

def index(request):
	rule_list = Rule.objects.all()

	return render_to_response('doc/index.html', {'rule_list': rule_list})

def detail(request, rule_name):
	rule = get_object_or_404(Rule, slug=rule_name)
	return render_to_response('doc/detail.html', {'rule': rule})