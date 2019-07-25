from flask import Flask, jsonify
app = Flask(__name__) # Initialized a flask app


@app.route('/')
def hello():
    return jsonify(
        {"message": 'Hello youre welcom'}
    )


if __name__ == '__main__':
    app.run(debug=True)## Shows all error messages and bugs