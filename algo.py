from flask import jsonify, request

def algo_webhook(request):
    data = request.json
    print("algo data = "+data)
    return jsonify({"status": "success", "message": request.json})
