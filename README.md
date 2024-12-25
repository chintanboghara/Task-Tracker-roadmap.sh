# Task Tracker CLI

Task Tracker CLI is a lightweight command-line application to manage and track tasks efficiently. It uses a simple JSON file for data storage and provides commands to add, update, delete, and list tasks.

## Features

- Add tasks with a description.
- Update task descriptions.
- Delete tasks by ID.
- Mark tasks as `todo`, `in-progress`, or `done`.
- List all tasks or filter by their status.

## Installation

### Prerequisites
- Python 3.7 or higher installed on the system.

### Steps

Create an empty `tasks.json` file in the project directory:
   ```bash
   echo "[]" > tasks.json
   ```

## Usage

Run the CLI with the following commands:

### Adding a Task
```bash
python task_cli.py add "Buy groceries"
```

### Updating a Task
```bash
python task_cli.py update <task_id> "Updated task description"
```

### Deleting a Task
```bash
python task_cli.py delete <task_id>
```

### Marking a Task
- Mark a task as in progress:
  ```bash
  python task_cli.py mark-in-progress <task_id>
  ```
- Mark a task as done:
  ```bash
  python task_cli.py mark-done <task_id>
  ```

### Listing Tasks
- List all tasks:
  ```bash
  python task_cli.py list
  ```
- List tasks by status:
  ```bash
  python task_cli.py list todo
  python task_cli.py list in-progress
  python task_cli.py list done
  ```

## Task Properties

Each task contains the following properties:
- **id**: Unique identifier for the task.
- **description**: A brief description of the task.
- **status**: The current status (`todo`, `in-progress`, `done`).
- **createdAt**: Timestamp of task creation.
- **updatedAt**: Timestamp of the last update.
