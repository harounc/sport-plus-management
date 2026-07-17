from datetime import date
from django.db import migrations

def seed(apps, schema_editor):
    Fondateur = apps.get_model("pages", "Fondateur")
    Joueur = apps.get_model("joueurs", "Joueur")
    Actualite = apps.get_model("actualites", "Actualite")
    founders = [
        ("Lamine Diallo", "Agent licencié FIFA — Fondateur", "Fondateur de Sport Plus Management, il met son réseau et son expertise du football professionnel au service des joueurs qu’il représente."),
        ("[Associé 2 — nom à venir]", "Rôle à préciser", "Biographie provisoire — à compléter avec les informations fournies par le client avant mise en ligne."),
        ("[Associé 3 — nom à venir]", "Rôle à préciser", "Biographie provisoire — à compléter avec les informations fournies par le client avant mise en ligne."),
    ]
    for i, (nom, role, bio) in enumerate(founders): Fondateur.objects.get_or_create(nom=nom, defaults={"role": role, "bio": bio, "ordre": i})
    players = [
        ("Yannick Koffi","yannick-koffi","Gardien",date(2004,3,12),"ASEC Mimosas","Côte d’Ivoire","Droit",34,0,1,True,"Gardien agile et bon jeu au pied, Yannick s’est imposé comme titulaire indiscutable. Sa lecture du jeu apporte de la sérénité à toute la défense."),
        ("Moussa Traoré","moussa-traore","Défenseur",date(2002,1,8),"FC Nordsjælland","Mali","Droit",41,2,3,True,"Défenseur central puissant et bon relanceur, Moussa évolue en première division danoise où il s’est rapidement imposé comme titulaire."),
        ("Aboubacar Sylla","aboubacar-sylla","Défenseur",date(2005,6,19),"Étoile du Sahel","Guinée","Gauche",22,1,2,False,"Latéral gauche offensif à fort potentiel, Aboubacar attire l’attention de plusieurs clubs européens."),
        ("Jean-Eudes Aka","jean-eudes-aka","Milieu",date(2003,2,14),"Stade Rennais","Côte d’Ivoire","Droit",38,5,8,True,"Milieu relayeur complet, Jean-Eudes s’illustre par sa capacité à récupérer et distribuer le jeu avec justesse."),
        ("Karim Ouattara","karim-ouattara","Milieu",date(2006,5,4),"RC Lens","Côte d’Ivoire","Gauche",15,2,4,False,"Jeune milieu créatif formé au centre de formation, Karim est considéré comme l’un des grands espoirs de sa génération."),
        ("Didier N’Guessan","didier-nguessan","Attaquant",date(2001,9,21),"KAA Gent","Côte d’Ivoire","Droit",33,19,6,True,"Attaquant de pointe au sens du but affirmé, Didier termine meilleur buteur de son club sur les deux dernières saisons."),
        ("Samuel Boakye","samuel-boakye","Attaquant",date(2004,7,11),"Royal Antwerp","Ghana","Droit",27,11,5,False,"Ailier rapide et percutant, Samuel excelle dans le un-contre-un et apporte une réelle profondeur offensive."),
        ("Ibrahim Cissé","ibrahim-cisse","Gardien",date(2000,4,2),"AS Vita Club","Sénégal","Gauche",29,0,0,False,"Gardien expérimenté réputé pour ses réflexes et son autorité dans la surface, Ibrahim recherche un nouveau défi à l’international."),
    ]
    for order,p in enumerate(players):
        Joueur.objects.get_or_create(slug=p[1], defaults={"nom":p[0],"poste":p[2],"date_naissance":p[3],"club_actuel":p[4],"nationalite":p[5],"pied_fort":p[6],"matchs":p[7],"buts":p[8],"passes_decisives":p[9],"mis_en_avant":p[10],"description":p[11],"ordre":order})
    news = [
        ("Jean-Eudes Aka signe au Stade Rennais","jean-eudes-aka-signe-au-stade-rennais",date(2026,7,2),"Notre milieu de terrain rejoint le championnat français pour la nouvelle saison.","Jean-Eudes Aka s’engage avec le Stade Rennais pour les trois prochaines saisons. Sport Plus Management se réjouit de ce nouveau chapitre et remercie l’ensemble des parties prenantes ayant permis la conclusion de cet accord."),
        ("Sport Plus Management partenaire de l’Abidjan Cup","sport-plus-management-partenaire-abidjan-cup",date(2026,6,18),"Notre agence s’associe au tournoi pour repérer de nouveaux talents.","Sport Plus Management devient partenaire officiel de l’Abidjan Cup, un tournoi qui réunit chaque année les meilleurs jeunes talents de la sous-région. L’occasion pour l’agence de renforcer son réseau de détection."),
        ("Didier N’Guessan buteur décisif pour KAA Gent","didier-nguessan-buteur-decisif",date(2026,6,3),"Un doublé qui confirme sa belle forme en championnat belge.","Auteur d’un doublé lors de la dernière journée de championnat, Didier N’Guessan confirme sa montée en puissance et s’impose comme l’un des attaquants les plus en forme du championnat belge."),
    ]
    for n in news: Actualite.objects.get_or_create(slug=n[1], defaults={"titre":n[0],"date":n[2],"extrait":n[3],"contenu":n[4]})

class Migration(migrations.Migration):
    dependencies = [("pages","0001_initial"),("joueurs","0001_initial"),("actualites","0001_initial")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
