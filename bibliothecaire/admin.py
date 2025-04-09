from django.contrib import admin
from .models import Membre, Media, Livre, CD, DVD, JeuDePlateau

admin.site.register([Membre])
admin.site.register([Livre])

admin.site.register([CD])
admin.site.register([DVD])
admin.site.register([Media])
admin.site.register([JeuDePlateau])


# Register your models here.
