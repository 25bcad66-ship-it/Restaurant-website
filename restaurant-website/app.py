from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Backend is running succesfully"

# 🔗 Use Render DATABASE_URL (set this in environment variables)
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Create table (run once automatically)
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            message TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

create_table()

# ✅ Save data
@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Data saved successfully!"})

# ✅ View all data
@app.route('/contacts', methods=['GET'])
def get_contacts():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    contacts = []
    for row in rows:
        contacts.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "message": row[3]
        })

    return jsonify(contacts)

if __name__ == '__main__':
    app.run(debug=True)
