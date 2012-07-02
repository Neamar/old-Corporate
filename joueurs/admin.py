from joueurs.models import Player, Share
from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
    list_display= ('name', 'pc')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Share)
