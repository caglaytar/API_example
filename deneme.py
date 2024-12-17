from flask import Flask,request,jsonify

app = Flask(__name__)

tasks = []

@app.route ('/api/tasks', methods=["GET"])
def get_tasks ():
    return jsonify(tasks)

@app.route ('/api/tasks',methods=["POST"])
def add_task():
    task = request.get_json()
    if 'title' not in task:
        return jsonify ({"error":"title not found"})
    task["id"] = len(tasks) +1
    task["completed"] = False
    tasks.append(task), 201

@app.route('/api/tasks/<int:task_id>',methods=["PUT"])
def update_task():
    task = next((task for task in tasks if task["id"]) == task_id), None
    if task:
        data = request.get_json()
        task.update(data)
        return jsonify(task)
    return jsonify({"error":"Task not found"})

if __name__ == '__main__':
    app.run(debug=True)