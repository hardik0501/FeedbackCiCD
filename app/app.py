from flask import Flask, request, render_template, jsonify
import json
from datetime import datetime

app = Flask(__name__)

feedback_data = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")
    feedback_data.append({
        "name": name,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return render_template("index.html", success=True)

@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
