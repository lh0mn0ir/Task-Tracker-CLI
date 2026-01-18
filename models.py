import controllers
from datetime import datetime
# Object task

DATA = controllers.load()

class Task:
    def __init__(self,  description, status):
        self.id = len(DATA)+1
        self.description = description
        self.status = status
        self.createdAt = datetime.now().strftime("%d/%m/%Y, %H:%M")
        self.updateAt = datetime.now().strftime("%d/%m/%Y, %H:%M")

    def __str__(self):
        return self.description

    def add_task(self):
        global DATA
        task = {"id": self.id,
                "description": self.description,
                "status": self.status,
                "createdAt": self.createdAt,
                "updatedAt": self.updateAt
                }
        DATA.append(task)
        controllers.save(DATA)

    @staticmethod
    def update_task(id_task:int, data:dict):
            # Charger les données actuelles
            for idx, task in enumerate(DATA):
                if task["id"] == id_task:
                    # Mettre à jour les champs si présents dans data
                    task["description"] = data.get("description", task["description"])
                    task["status"] = data.get("status", task["status"])
                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M")
                    DATA[idx] = task
                    controllers.save(DATA)
                    print("Sauvegarde éffectuée")
                    return True
            return False

    @staticmethod
    def delete_task(id_task):
        for idx, task in enumerate(DATA):
            if task["id"] == id_task:
                DATA.pop(idx)