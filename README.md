# MODELISATION D'UN PARCOURS OPPORTUNISTE D'ITINERAIRES

Ceci est un guide détaillée sur les étapes et les dépendances nécessaires pour lancer notre projet, réalisé avec le Framework Django et une base de données SQlite, nous groupe 11 de la 4GI à l'Ecole Nationale Supérieure Polytechnique de Yaoundé, pour le compte de l'**UE Administration Réseaux**:

## Guide d'utilisation

Notre projet utilise la base de données SQLite, et est réalisé entièrement avec le langage de programmation **Python**

### Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python (version 3.7 ou supérieure)
- pip (un gestionnaire de packages Python)

### Installation

Suivez les étapes ci-dessous pour installer les dépendances nécessaires et configurer le projet Django :

1. Accédez au répertoire du projet :

   ```bash
   cd <CHEMIN_VERS_LE_RÉPERTOIRE>
   ```

2. (Optionnel) Créez un environnement virtuel pour isoler les dépendances du projet:

   ```bash
   python -m venv env
   source env/bin/activate
   ```
   NB: vous pouvez aussi vous en passer, si vous avez déjà Django déjà installé sur votre machine. Plus d'informations sur les environnements virtualisés ici https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/development_environment

3. Installez les dépendances du projet à l'aide de pip :

   ```bash
   pip install django crispy-forms
   ```
NB: Vous pouvez aussi consulter les dépendances spécifiées dans la section INSTALLED_APPS de settings.py de path`./inventoryproject/settings.py`.

Pour plus d'informations sur le Framework Django, aller à https://docs.djangoproject.com/fr/5.0/

### Configuration de la base de données

Le projet est configuré pour utiliser SQLite par défaut. Suivez les étapes ci-dessous pour configurer la base de données :

1. Créez une nouvelle base de données SQLite en utilisant la commande suivante :

   ```bash
   python manage.py migrate
   ```

2. (Optionnel) Si vous souhaitez préremplir la base de données avec des données de test, exécutez la commande suivante :

   ```bash
   python manage.py loaddata initial_data
   ```

### Lancement du serveur de développement

Pour lancer le serveur de développement Django, suivez les étapes ci-dessous :

1. Exécutez la commande suivante pour démarrer le serveur :

   ```bash
   python manage.py runserver 8001
   ```

2. Accédez à l'URL suivante dans votre navigateur :

   ```bash
   http://localhost:8001/
   ```

### Création d'un compte administrateur

Suivez les étapes ci-dessous pour créer un compte administrateur :

1. Ouvrez une nouvelle fenêtre de terminal et exécutez la commande suivante pour créer un compte administrateur :

   ```bash
   python manage.py createsuperuser
   ```

2. Vous serez invité à fournir un nom d'utilisateur, une adresse e-mail (facultatif) et un mot de passe pour le compte administrateur. Remplissez les informations demandées.

3. Une fois que vous avez fourni les informations requises, le compte administrateur sera créé avec succès.

4. Accédez à l'URL suivante dans votre navigateur :

   ```browser
   http://localhost:8001/admin/
   ```

5. Connectez-vous en utilisant les informations d'identification du compte administrateur que vous avez créé précédemment.

6. Vous serez redirigé vers le tableau de bord d'administration Django, où vous pouvez gérer les modèles de données, les utilisateurs et effectuer d'autres tâches d'administration.

7. Il est aussi à noter que, vous pourrez vous connecter aussi bien à l'interface d'utilisateur, qu'à celui d'administration avec vos identifiants.

### Dépendances supplémentaires

Vous devez suivre les étapes supplémentaires suivantes :

1. Assurez-vous que vous avez déjà installé les dépendances du projet comme indiqué précédemment.

2. Rassurez vous que "crispy_forms" est dans la liste des applications installées dans le fichier de path `./inventoryproject/settings.py`, sinon aller à 4 :

   ```python
   INSTALLED_APPS = [
       ...
       'crispy_forms',
       ...
   ]
   ```

3. Configurez Crispy Forms en ajoutant le paramètre `CRISPY_TEMPLATE_PACK` s'il n'y est pas déjà présent dans le fichier de path `./inventoryproject/settings.py` :

   ```python
   CRISPY_TEMPLATE_PACK = 'bootstrap4'
   ```

4. Vous pouvez installer les dépendances crispy-forms et Django directement car elles sont nécessaires pour lancer le projet en utilisant la commande:

   ```bash
   pip install django crispy-forms
   ```
5. Installer toutes les dependances suivantes:

   ```bash
    pandas
    scikit-learn
    pickle
    crispy-forms
   ```

### Utilisation du projet

Une fois que le serveur de développement est en cours d'exécution, vous pouvez accéder aux différentes fonctionnalités du projet via l'interface utilisateur.

Vous pouvez vous connecter directement en tant qu'**utilisateur** pour avoir accès aux diverses fonctionnalités du projet ceci saisissant les identifiants suivants:

1. **Nom d'utilisateur: groupe11**
2. **Mot de passe: toto0000** 

Vous pouvez également créer votre propre compte administrateur comme suit:

### Création d'un compte administrateur

Suivez les étapes ci-dessous pour créer un compte administrateur dans votre projet Django :

1. Assurez-vous que le serveur de développement Django est en cours d'exécution.

2. Ouvrez une nouvelle fenêtre de terminal et exécutez la commande suivante pour créer un compte administrateur :

   ```bash
   python manage.py createsuperuser
   ```

3. Vous serez invité à fournir un nom d'utilisateur, une adresse e-mail (facultatif) et un mot de passe pour le compte administrateur. Remplissez les informations demandées.

4. Une fois que vous avez fourni les informations requises, le compte administrateur sera créé avec succès.

5. Accédez à l'URL suivante dans votre navigateur :

   ```browser
   http://localhost:8001/admin/
   ```

6. Connectez-vous en utilisant les informations d'identification du compte administrateur que vous avez créé précédemment.

7. Vous serez redirigé vers le tableau de bord d'administration Django, où vous pouvez gérer les modèles de données, les utilisateurs et effectuer d'autres tâches d'administration.

N'oubliez pas de consulter la documentation de Django pour plus d'informations sur la gestion de l'administration et des utilisateurs.

## Conclusion

Vous avez maintenant installé et configuré avec succès le projet. N'hésitez pas à explorer davantage la documentation officielle de Django pour en savoir plus sur ses fonctionnalités avancées ou en cas de succcès!
Lien vers la documentation de Django : https://docs.djangoproject.com/fr/5.0/