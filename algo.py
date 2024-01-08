from flask import jsonify, request

def algo_webhook(request):
    data = request.json

    return jsonify({"status": "success", "message": request.json})
