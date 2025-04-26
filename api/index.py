from flask import Flask, jsonify
from mangum import Mangum

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# Vercel expects a "handler"
handler = Mangum(app)
