from flask import Flask, request, jsonify

app = Flask (__name__)

product = []

@app.route('/', methods = ['GET'])
def get_product():
    return jsonify(product)

@app.route('/api', methods=['POST'])
def add_product():
    product = request.get_json()
    if 'title' not in product:
        return jsonify ({"error":"title not found"})
    product["id"] = len(product) +1
    product["completed"] = False
    product.append(product), 201

@app.route('/api/put',methods=['PUT'])
def update_product():
    product1 = next((product for product in product1 if product["id"]) == product_id), None
    if product:
        data = request.get_json()
        product.update(data)
        return jsonify(product)
    return jsonify({"error":"Task not found"})

if __name__ == '__main__':
    app.run(debug=True)

