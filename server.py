from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "你的_Gemini_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("text")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": user_query}]}]
    }
    res = requests.post(url, json=payload)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(port=5000)
