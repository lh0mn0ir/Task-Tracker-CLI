"""
Module models.py : contient la classe Task et les fonctions utilitaires pour gérer les tâches.
"""

import storage
from datetime import datetime


# Classe représentant une tâche du gestionnaire de tâches
class Task:
    def __init__(self, description, status="todo"):
        """
        Initialise une nouvelle tâche avec une description, un statut (par défaut 'todo'),
        une date de création et une date de mise à jour. L'identifiant est généré automatiquement.
        """
        self.id = self._generate_id()
        self.description = description
        self.status = status
        self.createdAt = datetime.now().strftime("%d/%m/%Y, %H:%M")
        self.updatedAt = self.createdAt

    @staticmethod
    def _generate_id():
        """
        Génère un nouvel identifiant unique pour chaque tâche en prenant le maximum
        des identifiants existants et en ajoutant 1. Si aucune tâche n'existe, retourne 1.
        """
        data = storage.load()
        if not data:
            return 1
        return max(task.get("id", 0) for task in data) + 1

    def __str__(self):
        return self.description

    def add_task(self):
        data = storage.load()
        task = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
        data.append(task)
        storage.save(data)

    @staticmethod
    def update_task(id_task: int, update_data: dict):
        data = storage.load()
        for idx, task in enumerate(data):
            if task.get("id") == id_task:
                task["description"] = update_data.get(
                    "description", task["description"]
                )
                task["status"] = update_data.get("status", task["status"])
                task["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M")
                data[idx] = task
                storage.save(data)
                print("Modifications éffectuées")
                return True
        return False

    @staticmethod
    def delete_task(id_task):
        data = storage.load()
        for idx, task in enumerate(data):
            if task.get("id") == id_task:
                data.pop(idx)
                storage.save(data)
                print("tâche supprimée")
                return True
        return False


def change_status(id_task, status):
    return Task.update_task(id_task, {"status": status})


# Fonction pour afficher toutes les tâches enregistrées
def list_all_task():
    """
    Affiche toutes les tâches présentes dans la base de données.
    """
    data = storage.load()
    for task in data:
        for key, value in task.items():
            print(key, ":", value)
        print()


# Fonction pour filtrer les tâches selon un statut donné
def filter_task_by(filter: str):
    """
    Affiche les tâches dont le statut correspond au filtre passé en paramètre.
    """
    data = storage.load()
    for task in data:
        if task.get("status") == filter:
            for key, value in task.items():
                print(key, ":", value)
            print()