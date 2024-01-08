import json
from flask import jsonify, request
from telegram_bot import telegram_message

def algo_webhook(request):
    data = request.json
    data_str = json.dumps(data, indent=4)
    print("algo data : " + data_str)
    telegram_message(request)
    return jsonify({"status": "success", "message": request.json})
