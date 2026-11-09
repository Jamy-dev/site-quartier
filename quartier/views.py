from django.views.generic import TemplateView

IMG = "quartier/img/"

# Pour ajouter une photo : mets le fichier dans quartier/static/quartier/img/
# puis ajoute une ligne ici.
PHOTOS = {
    "drapeau": {
        "fichier": IMG + "foot-drapeau.jpg",
        "titre": "Un supporter, un drapeau",
        "texte": "Dans les tribunes du stade, le drapeau du Guédiawaye FC flotte haut : « Guédiawaye avant tout ».",
        "credit": "@mrpii_25 (Pii Jr Photographe)",
    },
    "tribune": {
        "fichier": IMG + "foot-tribune.jpg",
        "titre": "Une tribune en feu",
        "texte": "Fumigènes bleus et jaunes, banderole géante : « Guédiawaye moy Sénégal ».",
        "credit": "@footmodi",
    },
    "mosquee": {
        "fichier": IMG + "mosquee.jpg",
        "titre": "La grande mosquée",
        "texte": "Ses minarets blancs et verts dominent le quartier.",
        "credit": "@khalil_mbaye221",
    },
    "place": {
        "fichier": IMG + "place-publique.jpg",
        "titre": "La place publique",
        "texte": "Bassin Bi Fitness Club : un espace de rencontre et de sport, entouré d'arbres en fleurs.",
        "credit": "@nourou_visuel",
    },
    "brt_mosquee": {
        "fichier": IMG + "brt-mosquee.jpg",
        "titre": "Le BRT et la mosquée",
        "texte": "Les bus du BRT passent devant la grande mosquée.",
        "credit": "@khalil_mbaye221",
    },
    "brt": {
        "fichier": IMG + "brt.jpg",
        "titre": "La station du BRT",
        "texte": "La voie du BRT et sa station, au quotidien.",
        "credit": "@diarutoo",
    },
}


class AccueilView(TemplateView):
    template_name = "quartier/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        p = PHOTOS
        ctx["hero"] = p["tribune"]
        ctx["foot"] = [p["drapeau"], p["tribune"]]
        ctx["lieux"] = [p["mosquee"], p["place"], p["brt_mosquee"], p["brt"]]
        ctx["credits"] = sorted({ph["credit"] for ph in p.values()})
        return ctx
