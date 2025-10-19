# Skills (Technical README)

Résumé
Ce dépôt contient plusieurs petits outils et démonstrations liés à la cybersécurité / développement web : une petite application Flask d'authentification, un script d'encryption démonstratif et un script de web scraping utilisant Selenium. Ce README technique décrit le rôle de chaque fichier, comment les exécuter, dépendances, et recommandations d'amélioration / sécurité.

Statut : prototype / démonstration (non prêt pour production)

Table des matières
- [Structure du dépôt](#structure-du-dépôt)
- [Description technique des fichiers](#description-technique-des-fichiers)
- [Prérequis et dépendances](#prérequis-et-dépendances)
- [Installation et exécution](#installation-et-exécution)
  - [Application Flask (app.py)](#application-flask-apppy)
  - [Script d'encryption (real_encryption.py)](#script-dencryption-real_encryptionpy)
  - [Script de scraping (web_scrapping.py)](#script-de-scraping-web_scrappingpy)
- [Sécurité et points d'attention](#sécurité-et-points-dattention)
- [Améliorations recommandées](#améliorations-recommandées)
- [Tests & développement](#tests--développement)
- [Licence & contact](#licence--contact)

Structure du dépôt (fichiers clés)
- app.py — petite application Flask (inscription / connexion) avec stockage SQLite.
- register.html, login.html — templates HTML pour les pages d'enregistrement / connexion (à placer dans templates/).
- style.css — feuille de style (à placer dans static/).
- real_encryption.py — démonstration d'utilisation de cryptography.Fernet : génération de clé, chiffrement / déchiffrement.
- web_scrapping.py — script Selenium (Firefox) qui récupère noms et commentaires d'une page exemple et écrit dans un fichier texte.
- README.md — ce fichier.

Description technique des fichiers

- app.py
  - Framework : Flask + Flask-Bcrypt.
  - Fonctionnalités :
    - Initialise une base SQLite `db.sqlite` (table users) au démarrage.
    - Routes :
      - / : page d'accueil (retourne simplement "Home Page").
      - /register [GET, POST] : formulaire d'inscription. Le mot de passe est haché avec bcrypt puis inséré dans la base.
      - /login [GET, POST] : vérification des identifiants. Si OK, id utilisateur en session.
      - /logout : efface la session.
  - Points techniques :
    - La base est créée par un connect au niveau module (bloc d'initialisation).
    - Secret Flask défini dans le code (app.secret_key = "your_secret_key").
    - Utilise sqlite3 directement (requêtes paramétrées pour l'insertion / recherche).
    - Rendu des templates `register.html` et `login.html` — Flask attend un répertoire templates/ contenant ces fichiers.

- register.html / login.html
  - Templates simples HTML pour les formulaires d'inscription / connexion.
  - Utilisent `{{ url_for('static', filename='style.css') }}` pour charger `style.css`.
  - À placer dans templates/register.html et templates/login.html respectivement.

- style.css
  - Feuille de style pour les formulaires (prévue dans static/style.css).
  - Contient styles de base : centrage, style des boutons, champs, etc.

- real_encryption.py
  - Utilise cryptography.fernet.Fernet.
  - Fonctions :
    - generate_key() → écrit `encryption_key.key` en binaire.
    - load_key() → lit la clé.
    - encrypt_text(plain_text, key) → retourne le texte chiffré.
    - decrypt_text(cipher_text, key) → retourne le texte déchiffré.
  - main() : génère la clé, chiffre un message d'exemple, puis le déchiffre et affiche les résultats.
  - Comportement : crée un fichier `encryption_key.key` dans le répertoire courant.

- web_scrapping.py
  - Utilise Selenium WebDriver (Firefox).
  - Ouvre la page `http://testphp.vulnweb.com/artists.php` et récupère, pour i allant 1 à 3, les éléments trouvés via XPath :
    - artist_name : "/html/body/div/div[2]/div[{}]/a/h3"
    - artist_comment : "/html/body/div/div[2]/div[{}]/p/a"
  - Rassemble les noms et commentaires dans des listes puis écrit dans `data.txt` (chemin hardcodé dans le script : /home/jeanbrice/Documents/SkillsIntern/data.txt).
  - Ferme le driver après un sleep de 3s.
  - Points techniques :
    - Requiert geckodriver et Firefox installés et accessibles dans le PATH.
    - XPath rigide (fragile si structure HTML change).
    - Chemin de sortie hardcodé → à paramétrer.

Prérequis et dépendances
- Python 3.8+
- Packages Python :
  - flask
  - flask-bcrypt
  - cryptography
  - selenium
- Système :
  - Firefox installé
  - geckodriver (compatible avec la version de Firefox) — dans le PATH
- Optionnel : virtualenv/venv

Exemple d'installation (Linux/macOS)
1. Clone
   git clone https://github.com/cyber-pnl/Skills.git
   cd Skills

2. Créer et activer un environnement virtuel
   python3 -m venv .venv
   source .venv/bin/activate

3. Installer dépendances
   pip install flask flask-bcrypt cryptography selenium

(Remplacez par `pip install -r requirements.txt` si vous ajoutez un requirements.txt.)

Exécution — détails

- Application Flask (dev)
  - Préparation :
    - Créer l'arborescence attendue :
      - mv register.html templates/register.html
      - mv login.html templates/login.html
      - mv style.css static/style.css
  - Lancer :
    - python app.py
    - ou :
      export FLASK_APP=app.py
      export FLASK_ENV=development
      flask run
  - Base : un fichier `db.sqlite` est créé automatiquement. Pour réinitialiser, supprimez `db.sqlite`.

- real_encryption.py
  - Lancer :
    - python real_encryption.py
  - Résultat :
    - Génère `encryption_key.key` et affiche l'original, le chiffré et le déchiffré dans la console.
  - Note : ne commitez pas `encryption_key.key` dans le dépôt.

- web_scrapping.py
  - Pré-requis : Firefox + geckodriver en PATH.
  - Modifier dans le script :
    - file_path → chemin de sortie souhaité (ne pas écrire dans un dossier personnel non partagé).
    - éventuellement rendre le navigateur headless via options.
  - Lancer :
    - python web_scrapping.py
  - Résultat : écrit les noms et commentaires extraits dans le fichier défini.

Sécurité et points d'attention (important)
- app.secret_key est hardcodé dans app.py — remplacer par une variable d'environnement (ex. FLASK_SECRET) en production.
- Pas de protection CSRF pour les formulaires (utiliser Flask-WTF / CSRFProtect).
- Clé d'encryption (`encryption_key.key`) est écrite sur disque — ne la stockez pas dans le dépôt Git. Ajoutez-la à .gitignore.
- web_scrapping :
  - XPath est fragile ; préférez des sélecteurs CSS ou robustes.
  - Respecter le robots.txt et conditions d'usage du site cible.
- Administration de la base SQLite :
  - SQLite convient pour prototyping ; en production, migrer vers une DB server (Postgres, MySQL).
- Validation des entrées : aujourd'hui minimale. Ajouter validation côté serveur et côté client.
- Sessions : configurer cookie_secure, cookie_httponly, SAME_SITE en production.

Améliorations recommandées
- Ajouter un requirements.txt et instructions Docker pour la reproductibilité.
- Déplacer la configuration (DB path, secret key, chemins) vers un fichier config ou variables d'environnement.
- Utiliser SQLAlchemy + Alembic pour gestion des migrations.
- Tests unitaires (pytest) pour logic d'encryption et routes Flask.
- Logging au lieu de prints.
- Modulariser l'application Flask (blueprints).
- Paramétrer web_scrapping pour accepter URL et sortie en CLI (argparse).

Exemples d'usage rapide
- Inscription / login (Flask)
  1. Démarrer Flask.
  2. Accéder à http://127.0.0.1:5000/register, créer un user.
  3. Se connecter sur /login.

- Tester chiffrement :
  python real_encryption.py

- Lancer scraping (après installation de geckodriver) :
  python web_scrapping.py

Fichiers à ajouter (conseillé)
- requirements.txt (exemple) :
  flask
  flask-bcrypt
  cryptography
  selenium
- .gitignore (exclure):
  .venv/
  encryption_key.key
  db.sqlite
  __pycache__/

Contact / auteur
- Repository : cyber-pnl/Skills
- Auteur : @cyber-pnl (GitHub)

Licence
- À préciser (ajouter un fichier LICENSE). Par défaut, ajoutez MIT si vous souhaitez autoriser la réutilisation.

Si vous voulez, je peux :
- Générer automatiquement un requirements.txt et un .gitignore.
- Réécrire web_scrapping.py pour accepter des arguments (URL, sorties) et exécuter Firefox en headless.
- Refactorer app.py pour utiliser une configuration et templates placés dans les bons dossiers, et ajouter CSRF / meilleures pratiques.
