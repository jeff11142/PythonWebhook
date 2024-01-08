from flask import Flask, request, jsonify, abort
from algo import algo_webhook

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)
    return jsonify({"message": "Webhook received!"})

@app.route('/algo', methods=['POST'])
def algo():
    return algo_webhook(request)

@app.route('/')
def index():
    return "Welcome to My Auto Trader"

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Route Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal Server Error"), 500

if __name__ == '__main__':
    app.run(debug=True, port=3001)
