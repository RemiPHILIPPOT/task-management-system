# Système de Gestion de Tâches avec Flask

Ce projet est un système simple de gestion de tâches développé avec Flask.

## Fonctionnalités

-   **Ajouter des tâches :** Les utilisateurs peuvent ajouter de nouvelles tâches avec un titre, une description et une priorité.
-   **Supprimer des tâches :** Les utilisateurs peuvent supprimer les tâches qu'ils ont créées.
-   **Notification par E-mail :** Les utilisateurs reçoivent une notification par e-mail pour les rappeler des tâches dues aujourd'hui.

## Installation

1. **Cloner le Repository :**

    ```bash
    git clone https://github.com/RemiPHILIPPOT/task-management-system.git
    ```

2. **Installer les Dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configurer les Paramètres :**

    - Creez le fichier `config.py` et configurez les paramètres comme `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`, `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD` selon vos besoins.

4. **Démarrer l'Application :**

    ```bash
    python run.py
    ```

L'application sera accessible à l'adresse http://localhost:5000 dans votre navigateur web.

## Utilisation

-   Accédez à l'application dans votre navigateur.
-   Ajoutez de nouvelles tâches en remplissant le formulaire.
-   Supprimez les tâches existantes en cliquant sur le bouton "Supprimer".
