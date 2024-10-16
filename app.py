from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory task list (for simplicity, using a dictionary)
tasks = {
    1: {"title": "Task One", "description": "First task", "due_date": "2024-12-01", "status": "pending"},
    2: {"title": "Task Two", "description": "Second task", "due_date": "2024-12-15", "status": "completed"}
}

# Helper function to check if task exists
def get_task_or_404(task_id):
    task = tasks.get(task_id)
    if not task:
        abort(404, description="Task not found")
    return task

# GET all tasks or specific task by ID
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_or_404(task_id)
    return jsonify(task)

# POST a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_id = max(tasks.keys()) + 1 if tasks else 1
    tasks[new_id] = {
        "title": data["title"],
        "description": data["description"],
        "due_date": data["due_date"],
        "status": data["status"]
    }
    return jsonify(tasks[new_id]), 201

# PUT to update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = get_task_or_404(task_id)
    data = request.json
    task.update({
        "title": data.get("title", task["title"]),
        "description": data.get("description", task["description"]),
        "due_date": data.get("due_date", task["due_date"]),
        "status": data.get("status", task["status"])
    })
    return jsonify(task)

# DELETE a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = get_task_or_404(task_id)
    del tasks[task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
