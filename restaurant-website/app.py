from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

# Create file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    new_entry = {
        "name": data.get("name"),
        "email": data.get("email"),
        "message": data.get("message")
    }

    # Read existing data
    with open(DATA_FILE, "r") as f:
        entries = json.load(f)

    # Add new entry
    entries.append(new_entry)

    # Save back to file
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=4)

    return jsonify({"message": "Data saved successfully!"})

@app.route('/data', methods=['GET'])
def get_data():
    with open(DATA_FILE, "r") as f:
        entries = json.load(f)
    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True)
