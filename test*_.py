from models import Task
import controllers

task = Task(description="cours de fonction", status="in-progress")
task.add_task()
Task.update_task(1, {"description": "cours algo","status":"done", "updatedAt":None})
print(controllers.get_task(1))