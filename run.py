from flask import Flask, jsonify, request
app = Flask(__name__) # Initialized a flask app


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(
        {"message": 'Hello your welcome'}
    )
    
@app.route('/hello', methods=['POST'])
def greetings():
    print(request.json)
    name = request.json['name']
    print(name)
    return jsonify(
            {"message": "Hello "+ name}
    )
if __name__ == '__main__':
    app.run(debug=True)## Shows all error messages and bugs


