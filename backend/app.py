from flask import Flask, jsonify
import pymysql
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_connection():
    return pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        db=os.environ['DB_NAME'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/api/titanic')
def get_titanic_data():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM titanic LIMIT 500")
            result = cursor.fetchall()
        return jsonify(result)
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

