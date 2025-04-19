from django.contrib import admin
from .models import Membre, Livre, CD, DVD, JeuDePlateau, Emprunt

admin.site.register(Membre)
admin.site.register(Livre)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(JeuDePlateau)
admin.site.register(Emprunt)


# Register your models here.
