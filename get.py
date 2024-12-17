from flask import Flask

app = Flask(__name__)

@app.route('/', 
           methods = ['GET'])

def create_resource():
    return ({"message": "GET request successful"})

if __name__ == '__main__':
    app.run(debug=True)
