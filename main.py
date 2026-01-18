#!/usr/bin/env python3
import sys
from models import Task, change_status, list_all_task, filter_task_by


def print_usage():
    print(
        """Usage:
	python main.py add "description"
	python main.py update <id> "new description" [status]
	python main.py delete <id>
	python main.py mark-in-progress <id>
	python main.py mark-done <id>
	python main.py list [status]
	status: todo | done | in-progress
	"""
    )


def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Description requise.")
            return
        description = sys.argv[2]
        t = Task(description)
        t.add_task()
        print(f"Tâche ajoutée avec succès (ID: {t.id})")

    elif command == "update":
        if len(sys.argv) < 4:
            print("ID et nouvelle description requis.")
            return
        try:
            id_task = int(sys.argv[2])
        except ValueError:
            print("ID invalide.")
            return
        description = sys.argv[3]
        status = sys.argv[4] if len(sys.argv) > 4 else None
        update_data = {"description": description}
        if status:
            update_data["status"] = status
        updated = Task.update_task(id_task, update_data)
        if updated:
            print("Tâche mise à jour.")
        else:
            print("Tâche non trouvée.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("ID requis.")
            return
        try:
            id_task = int(sys.argv[2])
        except ValueError:
            print("ID invalide.")
            return
        deleted = Task.delete_task(id_task)
        if not deleted:
            print("Tâche non trouvée.")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("ID requis.")
            return
        try:
            id_task = int(sys.argv[2])
        except ValueError:
            print("ID invalide.")
            return
        changed = change_status(id_task, "in-progress")
        if changed:
            print("Tâche marquée comme en cours.")
        else:
            print("Tâche non trouvée.")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("ID requis.")
            return
        try:
            id_task = int(sys.argv[2])
        except ValueError:
            print("ID invalide.")
            return
        changed = change_status(id_task, "done")
        if changed:
            print("Tâche marquée comme terminée.")
        else:
            print("Tâche non trouvée.")

    elif command == "list":
        if len(sys.argv) == 2:
            list_all_task()
        else:
            status = sys.argv[2]
            filter_task_by(status)

    else:
        print_usage()


if __name__ == "__main__":
    main()
