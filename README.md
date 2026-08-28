<h3>Task Manager CLI</h3>

A simple command-line task management application built with Python.
This project started as a small Python CLI application and evolved into a more structured version with separated responsibilities for the CLI, service layer, repository, storage, validation, and task model.
The main goal of this project is to practice Python fundamentals, object-oriented programming, application structure, data persistence, validation, exception handling, and working with JSON.

<h3>📌 About The Project</h3>

Task Manager CLI is a terminal-based application that allows users to manage their daily tasks without requiring a database or external service.
Tasks are persisted in a local JSON file, making the application simple to run and easy to understand.
The project includes common task-management operations such as:
Creating tasks
Listing all tasks
Searching tasks by title
Updating tasks
Completing tasks
Marking tasks as uncompleted
Deleting tasks
Viewing task statistics
The project is intentionally kept simple in terms of infrastructure so that the focus remains on Python programming and application design.

<h3>✨ Features</h3>

Create Task
Create a new task by providing:
Title
Description
New tasks are automatically created with the uncompleted status.
Each task also stores its creation date.
List Tasks
Display all stored tasks with information such as:
ID
Title
Description
Status
Creation date
Last update date
The list command also provides basic statistics about the tasks.
Example:
```py
=====================================
tasks
=====================================

all : 5
most status : uncompleted
completed : 2
uncompleted : 3
Search Tasks
Search for tasks by their title.
The search returns tasks whose title contains the provided search term.
```

<h3>Update Task</h3>

Update an existing task's:
Title
Description
Status
The application also updates the updated_at field when a task is modified.
Complete / Uncomplete Tasks
Tasks can be moved between two states:
completed
uncompleted
This allows the user to mark finished tasks and return them to an unfinished state when necessary.
Delete Task
Delete a task using its ID.
Task Statistics
The application provides basic statistics using Python's collections.Counter.
Current statistics include:
Total number of tasks
Most common task status
Number of completed tasks
Number of uncompleted tasks

<h3>🏗️ Project Structure</h3>

```py
task-manager-cli/
│
├── main.py
│
├── task.py
├── task_cli.py
├── task_service.py
├── task_repositori.py
├── json_storage.py
├── task_validation.py
├── exception.py
├── utility.py
│
└── data/
    └── data.json
```

<h3>🧩 Architecture</h3>

The project uses a simple layered structure to keep different responsibilities separated.

<h6>CLI Layer</h6>
task_cli.py
Responsible for interacting with the user through the terminal and selecting the requested operation.

<h6>Service Layer</h6>
task_service.py
Contains the application's main task operations and coordinates between validation and the repository.

<h6>Repository Layer</h6>
task_repositori.py
Responsible for retrieving and modifying task data.
It acts as the layer between the application's business operations and the storage system.

<h6>Storage Layer</h6>
json_storage.py
Handles reading and writing JSON data.
The storage logic is isolated from the rest of the application so that the persistence mechanism can be changed more easily in the future.

<h6>Validation</h6>
task_validation.py
Contains validation rules for task data, including:
Title length
Description length
Valid task status

<h6>Model</h6>
task.py
Defines the Task data model using Python's dataclass.
@dataclass
class Task:
id: int
title: str
description: str
status: str
created_at: str = None
updated_at: str = None

<h6>Exceptions</h6>
exception.py
Defines a custom TaskException for application-specific errors.

<h6>Utilities</h6>
utility.py
Contains helper functions used by different parts of the application, including:
Task serialization
Task statistics
CLI input
Task creation/update input handling

<h6>Data Storage</h6>
The application uses a local JSON file:
data/data.json
A task is stored in a structure similar to:
```json
{
"id": 1,
"title": "Learn Python",
"description": "Practice Python OOP",
"status": "uncompleted",
"created_at": "2026-08-27",
"updated_at": ""
}
```

No external database is required.

<h6>Installation</h6>

1. Clone the repository
   git clone https://github.com/YOUR_USERNAME/task-manager-cli.git
2. Enter the project directory
   cd task-manager-cli
3. Run the application
   python main.py
   Depending on your Python installation, you may need:
   python3 main.py


<h6>🖥 Usage</h6>

After starting the application, the CLI displays the available operations:

```py
   =====================================
   operations
   =====================================

1 - create task
2 - list task
3 - search task
4 - update task
5 - complecte task
6 - uncompleted task
7 - delete task
8 - close
```

Select an operation by entering its number.
Example
1
Then provide the task information:
create a new task:

name? Learn Python
description? Practice Python OOP
The task will be stored in data/data.json.

<h6>🧠 What I Practiced</h6>

This project was built as a practical Python learning project.
The main concepts practiced were:
Python classes
Object-Oriented Programming
dataclass
Type hints
Functions and methods
JSON file handling
File I/O
Exception handling
Custom exceptions
Input validation
Repository pattern
Service layer
Separation of responsibilities
Basic data analysis
collections.Counter
CLI application design
Date handling
CRUD operations

<h6>🔄 Version 2</h6>

This repository represents the second version of the project.
Compared with the initial version, Version 2 focuses more on structure and separation of responsibilities rather than simply adding more features.
The application was reorganized around separate components for:
CLI
Service
Repository
Storage
Validation
Model
Exception
Utilities
This made the project a practical exercise in moving from a simple script toward a more maintainable application structure.

<h6>🎯 Project Goals</h6>

The goal of this project is not to build a production-ready task management platform.
Instead, it was created to practice designing a small application with Python while gradually introducing concepts that are commonly used in larger backend projects.
The project also serves as a foundation for future improvements such as:
Automated tests
Better CLI input handling
More robust ID management
SQLite database support
Configuration management
Better error handling
Improved CLI experience

<h6>📚 Project Status</h6>

This project is an educational Python project and is currently focused on learning and experimentation.
It is intentionally simple and does not require a database, web server, or external dependencies.

<h6>👨‍💻 Author</h6>

Milad Rezai
Backend developer focused on PHP/Laravel and currently expanding into Python development.
GitHub:
https://github.com/milirezai

<h6>📄 License</h6>

This project is open source and available under the MIT License.