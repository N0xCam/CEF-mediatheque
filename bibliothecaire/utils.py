import json
import os
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

MEDIA_JSON_PATH = os.path.join(settings.BASE_DIR, 'bibliothecaire', 'fixtures', 'medias.json')

def exporter_medias_en_json():
    from .models import Livre, CD, DVD, JeuDePlateau

    livres = list(Livre.objects.all().values())
    cds = list(CD.objects.all().values())
    dvds = list(DVD.objects.all().values())
    jeux = list(JeuDePlateau.objects.all().values())

    medias = {
        "livres": livres,
        "cds": cds,
        "dvds": dvds,
        "jeux_de_plateau": jeux,
    }

    with open(MEDIA_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(medias, f, indent=4, cls=DjangoJSONEncoder)

def importer_medias_depuis_json():
    from .models import Livre, CD, DVD, JeuDePlateau

    if not os.path.exists(MEDIA_JSON_PATH):
        return

    with open(MEDIA_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data.get('livres', []):
        Livre.objects.get_or_create(**item)

    for item in data.get('cds', []):
        CD.objects.get_or_create(**item)

    for item in data.get('dvds', []):
        DVD.objects.get_or_create(**item)

    for item in data.get('jeux_de_plateau', []):
        JeuDePlateau.objects.get_or_create(**item)