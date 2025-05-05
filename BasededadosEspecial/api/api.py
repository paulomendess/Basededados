import os
from flask import Flask, jsonify, request, session, make_response
import psycopg2
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from itsdangerous import Serializer, BadSignature, SignatureExpired

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return conn

@app.route('/', methods=["GET"])
def home():
    return "Welcome to bijbhknk!"


if __name__ == '__main__':
    print("Starting Flask server...")
    print(".i.")
    app.run(debug=False)

   
