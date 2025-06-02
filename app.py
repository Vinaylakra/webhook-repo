from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["webhookDB"]
collection = db["events"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json
    print("Received data : ", payload)
    data = {}

    if event_type == 'push':
        data = {
            "action": "push",
            "author": payload['pusher']['name'],
            "from_branch": None,
            "to_branch": payload['ref'].split('/')[-1],
            "timestamp": payload['head_commit']['timestamp']
        }
    elif event_type == 'pull_request':
        pr = payload['pull_request']
        if payload['action'] == 'opened':
            data = {
                "action": "pull_request",
                "author": pr['user']['login'],
                "from_branch": pr['head']['ref'],
                "to_branch": pr['base']['ref'],
                "timestamp": pr['created_at']
            }
        elif payload['action'] == 'closed' and pr.get('merged'):
            data = {
                "action": "merge",
                "author": pr['user']['login'],
                "from_branch": pr['head']['ref'],
                "to_branch": pr['base']['ref'],
                "timestamp": pr['merged_at']
            }
        else:
            return '', 204
    else:
        return '', 204

    collection.insert_one(data)
    return jsonify({"msg": "stored"}), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find({}, {'_id': 0}).sort('timestamp', -1).limit(10))
    return jsonify(events)


if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, port=5000)
