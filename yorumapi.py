from flask import Flask, request, jsonify

app = Flask (__name__)

comments = []

@app.route('/', methods = ['GET'])
def get_comments():
    return jsonify(comments)

@app.route('/api', methods=['POST'])
def add_comments():
    comments = request.get_json()
    if 'title' not in comments:
        return jsonify ({"error":"title not found"})
    comments["id"] = len(comments) +1
    comments["completed"] = False
    comments.append(comments), 201

@app.route('/api/put',methods=['PUT'])
def update_comments():
    comments1 = next((comments for comments in comments1 if comments["id"]) == comments_id), None
    if comments:
        data = request.get_json()
        comments.update(data)
        return jsonify(comments)
    return jsonify({"error":"Task not found"})

if __name__ == '__main__':
    app.run(debug=True)
