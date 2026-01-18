import controllers

# Object task

DATA = controllers.load()

class Task:
    def __init__(self,  description, status):
        self.id = None
        self.description = description
        self.status = status
        self.createdAt = None
        self.updateAt = None

    def __str__(self):
        return self.description

    def add_task(self):
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
        task = controllers.get_task(id_task=id_task)
        task["description"] = data["description"] or task["description"]
        task["status"] = data["status"] or task["status"]
        task["updatedAt"] = data["updatedAt"]
        controllers.save(task)
