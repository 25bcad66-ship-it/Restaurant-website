from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    name = data['name']
    email = data['email']
    message = data['message']

    # Save to file
    with open("messages.txt", "a") as f:
        f.write(f"{name} | {email} | {message}\n")

    return jsonify({"message": "Message saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
