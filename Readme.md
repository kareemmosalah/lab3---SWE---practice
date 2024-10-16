# Task Management API

This is a simple Flask API to manage tasks in a project. It allows you to perform CRUD operations (Create, Read, Update, Delete) on tasks.

## Endpoints

### GET /tasks
Returns a list of all tasks.

### GET /tasks/:id
Returns the details of a specific task by ID.

### POST /tasks
Adds a new task to the project.
- Body:
  ```json
  {
    "title": "New Task",
    "description": "New task description",
    "due_date": "2024-12-31",
    "status": "pending"
  }
