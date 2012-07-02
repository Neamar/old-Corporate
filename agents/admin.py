from agents.models import Fixer, Yakuza, Agency, CROC
from django.contrib import admin

class AgentAdmin(admin.ModelAdmin):
	list_display=('name', 'friend', 'private_friend', 'foe', 'private_foe', 'loyalties')

admin.site.register(Fixer, AgentAdmin)
admin.site.register(Yakuza, AgentAdmin)
admin.site.register(Agency, AgentAdmin)
admin.site.register(CROC)
