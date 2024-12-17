from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource', 
           methods = ['POST'])

def create_resource():
    data = request.get_json()
    return jsonify ({"data": data,"message": "POST request successful"}), 201

if __name__ == '__main__':
    app.run(debug=True)
