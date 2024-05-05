Assurez-vous d'avoir Python et installez Django : 
   -pip install django
Pour lancer l'apps exécutez les commandes suivantes:
  -python manage.py makemigrations gestionfichier
  -python manage.py migrate
  -python manage.py runserver

Objectif : 

L'objectif de ce projet est de créer un site web où les utilisateurs peuvent créer, visualiser et supprimer des annonces accompagnées d'images.
Fonctionnalités clés :

Ajout d'annonces : Les utilisateurs peuvent ajouter de nouvelles annonces avec une description et des images associées.
Visualisation des annonces : Toutes les annonces sont affichées sur la page principale du site avec leurs images.
Suppression d'annonces : Les utilisateurs peuvent supprimer les annonces qu'ils ont ajoutées.
Gestion des utilisateurs : Les utilisateurs doivent s'inscrire et se connecter pour ajouter ou supprimer des annonces.


Explication de la partie pratique du projet :

Les Vues (Views) :
Dans Django, les vues sont des fonctions Python qui reçoivent des requêtes HTTP et renvoient des réponses HTTP.
Vous avez défini des vues pour chaque fonctionnalité de votre application, par exemple :
Une vue pour afficher la liste des annonces (photo_list).
Une vue pour ajouter une nouvelle annonce (upload_photo).
Une vue pour supprimer une annonce (delete_annonce).
Chaque vue utilise les modèles de données pour interagir avec la base de données.
Les Modèles (Models) :
Les modèles sont des classes Python qui définissent la structure des données dans votre application.
Vous avez défini des modèles pour représenter les annonces (Annonce) et les images associées (UploadImage).
Ces modèles sont utilisés pour stocker et récupérer des données à partir de la base de données.
Vous avez également utilisé des relations de clés étrangères pour lier les images aux annonces correspondantes.
Les Templates :
Les templates sont des fichiers HTML qui définissent la structure de vos pages web.
Vous avez créé des templates pour afficher les annonces (show_files.html), pour la page de profil (profile.html), pour la page de connexion (login.html) et pour la page d'inscription (signup.html).
Ces templates utilisent des balises Django pour intégrer des données dynamiques provenant des vues et pour créer des boucles et des conditions logiques.
Les URLs (URL patterns) :
Les URL patterns définissent les correspondances entre les URL entrantes et les vues à appeler.
Vous avez configuré les URL patterns dans votre fichier urls.py pour rediriger les requêtes HTTP vers les vues appropriées.
Par exemple, vous avez défini des patterns pour les vues photo_list, upload_photo, delete_annonce, etc.
Les Fichiers Statiques (Static Files) :
Les fichiers statiques comprennent les fichiers CSS, JavaScript, les images, etc., utilisés pour styliser et rendre votre site web interactif.
Vous avez organisé vos fichiers CSS dans un répertoire static/css et les avez inclus dans vos templates HTML pour styliser votre site web.
