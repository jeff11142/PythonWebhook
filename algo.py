import json
from flask import jsonify, request

def algo_webhook(request):
    data = request.json
    data_str = json.dumps(data, indent=4)
    print("algo data : " + data_str)
    return jsonify({"status": "success", "message": request.json})
