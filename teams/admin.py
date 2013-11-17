from django.contrib import admin
from models import Team, NewsFeeds, Gallery, UserInTeamNtoN

admin.site.register(Team)
admin.site.register(NewsFeeds)
admin.site.register(Gallery)
admin.site.register(UserInTeamNtoN)