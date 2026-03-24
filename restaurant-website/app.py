from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    print("New Contact:")
    print(name, email, message)

    return jsonify({"message": "Message received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
    @app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    name = data['name']
    email = data['email']
    message = data['message']

    with open("messages.txt", "a") as f:
        f.write(f"{name} | {email} | {message}\n")

    return jsonify({"message": "Message saved successfully!"})