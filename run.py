from flask import Flask, jsonify, request
app = Flask(__name__) # Initialized a flask app


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(
        {"message": 'Hello your welcome'}
    )
    
@app.route('/hello', methods=['POST'])
def greetings():
    # print(request.json)
    name = request.json['name']
    # print(name)
    return jsonify(
            {"message": "Hello "+ name}
    )

@app.route('/hello', methods=['PUT'])
def edit_name():
     # print(request.json)
    name = request.json['name']
    # print(name)
    return jsonify(
            {"message": "Hello "+ name}
    )
@app.route('/login', methods=['POST'])
def login():
    try:
        if not request.json or 'username' not in request.json or 'password' not in request.json:
            return jsonify({
            "error": "username and password are required"
        }) 
    except:
        return jsonify({
            "error": "You have provided an empty request body"
        })
    username = request.json['username']
    password = request.json['password']

    

    print(request.json['username'])

    return jsonify({
        "message": "message"
    })
    
@app.route('/signup', methods=['POST'])
def signup():
    try:
        if not request.json or 'username' not in request.json or 'password' not in request.json or 'phone' not in request.json:
             return jsonify({
                 "error": "username, password and phone are required"
            })
    except:
         return jsonify({
            "error": "You have provided an empty request body"
        })
    username = request.json['username']
    password = request.json['password']
    phone = request.json['phone']

    print(request.json['username'])

    return jsonify({
        "message": "message"
    })
if __name__ == '__main__':
    app.run(debug=True)## Shows all error messages and bugs


