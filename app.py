from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify(message=f"Hello, {name}! Welcome to our beautiful web app.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
