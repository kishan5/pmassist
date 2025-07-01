from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Replace this with actual agent logic or Lyzr SDK integration
def run_pm_board_assist(query):
    # Placeholder for now
    return f"Mock response to: '{query}' from PM Board Assist Agent."

@app.route("/", methods=["GET"])
def home():
    return "PM Board Assist is running."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Query field is required."}), 400

    # Process the query using agent logic
    response = run_pm_board_assist(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
