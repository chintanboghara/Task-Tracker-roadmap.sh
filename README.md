# Task Tracker CLI

[![Python CLI Workflow](https://github.com/chintanboghara/Task-Tracker-roadmap.sh/actions/workflows/python-app.yml/badge.svg)](https://github.com/chintanboghara/Task-Tracker-roadmap.sh/actions/workflows/python-app.yml)

Task Tracker CLI is a lightweight command-line application designed to help you manage and track your tasks with ease. Using a simple JSON file for data storage, the tool offers straightforward commands to add, update, delete, and list your tasks.

## Features

- **Add Tasks:** Create new tasks with a description.
- **Update Tasks:** Modify task descriptions.
- **Delete Tasks:** Remove tasks by their unique ID.
- **Status Management:** Mark tasks as:
  - `todo`
  - `in-progress`
  - `done`
- **Task Listing:** View all tasks or filter them based on their status.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chintanboghara/Task-Tracker-roadmap.sh.git
   cd Task-Tracker-roadmap.sh
   ```

2. **Create an empty JSON file for storing tasks:**

   ```bash
   echo "[]" > tasks.json
   ```

3. (Optional) Set up a [virtual environment](https://docs.python.org/3/tutorial/venv.html) and install any dependencies (if applicable).

## Usage

Run the CLI by invoking the `task_cli.py` script with various commands as described below:

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

### Marking a Task's Status

- **In Progress:**
  ```bash
  python task_cli.py mark-in-progress <task_id>
  ```
- **Done:**
  ```bash
  python task_cli.py mark-done <task_id>
  ```

### Listing Tasks

- **List All Tasks:**
  ```bash
  python task_cli.py list
  ```
- **Filter by Status:**
  - For tasks with status `todo`:
    ```bash
    python task_cli.py list todo
    ```
  - For tasks marked as `in-progress`:
    ```bash
    python task_cli.py list in-progress
    ```
  - For tasks marked as `done`:
    ```bash
    python task_cli.py list done
    ```

## Task Data Structure

Each task is stored as a JSON object with the following properties:

- **id:** Unique identifier for the task.
- **description:** A brief task description.
- **status:** The current status (`todo`, `in-progress`, or `done`).
- **createdAt:** Timestamp indicating when the task was created.
- **updatedAt:** Timestamp indicating the last time the task was updated.
