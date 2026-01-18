
# Task Tracker

## Description

Task Tracker est une application CLI simple pour gérer vos tâches quotidiennes. Vous pouvez ajouter, modifier, supprimer et filtrer vos tâches selon leur statut (à faire, en cours, terminée). Les tâches sont stockées dans un fichier JSON local.

## Fonctionnalités

- Ajouter une tâche
- Mettre à jour une tâche (description et statut)
- Supprimer une tâche
- Marquer une tâche comme "en cours" ou "terminée"
- Lister toutes les tâches ou filtrer par statut (todo, in-progress, done)

## Installation

1. Clonez le dépôt ou copiez les fichiers dans un dossier local.
2. Assurez-vous d'avoir Python 3 installé.
3. Placez-vous dans le dossier `task-tracker`.

## Utilisation

Lancez le programme principal avec python :

```bash
python main.py <commande> [arguments]
```

### Commandes disponibles

- **Ajouter une tâche**
    ```bash
    python main.py add "Description de la tâche"
    # Exemple : python main.py add "Acheter du pain"
    ```

- **Mettre à jour une tâche**
    ```bash
    python main.py update <id> "Nouvelle description" [statut]
    # Exemple : python main.py update 1 "Acheter du pain et du lait" done
    ```

- **Supprimer une tâche**
    ```bash
    python main.py delete <id>
    # Exemple : python main.py delete 1
    ```

- **Marquer une tâche comme en cours**
    ```bash
    python main.py mark-in-progress <id>
    # Exemple : python main.py mark-in-progress 2
    ```

- **Marquer une tâche comme terminée**
    ```bash
    python main.py mark-done <id>
    # Exemple : python main.py mark-done 2
    ```

- **Lister toutes les tâches**
    ```bash
    python main.py list
    ```

- **Lister les tâches par statut**
    ```bash
    python main.py list todo
    python main.py list done
    python main.py list in-progress
    ```

## Structure du projet

- `main.py` : programme principal CLI
- `models.py` : logique métier et gestion des tâches
- `storage.py` : gestion du stockage JSON
- `db.json` : base de données locale des tâches
- `test_*.py` : tests unitaires

## Exemple d'utilisation

```bash
# Ajouter une tâche
python main.py add "Faire les courses"
# Mettre à jour une tâche
python main.py update 1 "Faire les courses et le ménage" in-progress
# Marquer comme terminée
python main.py mark-done 1
# Lister toutes les tâches
python main.py list
# Lister les tâches terminées
python main.py list done
```

## Auteur

Projet réalisé par Lhomnoir.
