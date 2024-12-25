import json
import os
import sys
from datetime import datetime

FILE_PATH = "tasks.json"

def load_tasks():
    """
    Load tasks from the JSON file. If the file does not exist, return an empty list.
    """
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """
    Save the given tasks to the JSON file.
    """
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """
    Add a new task with the given description.
    """
    tasks = load_tasks()
    task_id = max([task["id"] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description):
    """
    Update the description of a task with the given ID.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task(task_id):
    """
    Delete a task with the given ID.
    """
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        print("Task deleted successfully.")

def change_status(task_id, new_status):
    """
    Change the status of a task with the given ID.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {new_status}.")
            return
    print("Task not found.")

def list_tasks(status=None):
    """
    List tasks. If a status is provided, filter tasks by that status.
    """
    tasks = load_tasks()
    filtered_tasks = tasks if not status else [task for task in tasks if task["status"] == status]
    for task in filtered_tasks:
        print(f"[{task['status'].upper()}] {task['id']}: {task['description']}")
    if not filtered_tasks:
        print("No tasks found.")

def main():
    """
    Main entry point for the CLI application. Parse and execute commands.
    """
    args = sys.argv[1:]
    if not args:
        print("Usage: task-cli <command> [options]")
        return

    command = args[0]
    if command == "add" and len(args) > 1:
        add_task(" ".join(args[1:]))
    elif command == "update" and len(args) > 2:
        update_task(int(args[1]), " ".join(args[2:]))
    elif command == "delete" and len(args) > 1:
        delete_task(int(args[1]))
    elif command == "mark-in-progress" and len(args) > 1:
        change_status(int(args[1]), "in-progress")
    elif command == "mark-done" and len(args) > 1:
        change_status(int(args[1]), "done")
    elif command == "list":
        status = args[1] if len(args) > 1 else None
        list_tasks(status)
    else:
        print("Unknown command or invalid arguments.")

if __name__ == "__main__":
    main()
