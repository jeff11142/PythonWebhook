import json
from flask import jsonify, request
from telegram_bot import telegram_message

def algo_webhook(request):
    data = request.json
    data_str = json.dumps(data, indent=4)
    print("algo data : " + data_str)

    prefix = ""
    basecurrency = ""
    currency = ""
    side = ""
    entry = ""
    tp1 = ""
    tp2 = ""
    tp3 = ""
    tp4 = ""
    stop = ""

    if 'prefix' in data:
        prefix =  data['prefix']
    
    if 'basecurrency' in data:
        basecurrency =  data['basecurrency']

    if 'currency' in data:
        currency =  data['currency']

    if 'side' in data:
        side =  data['side']

    if 'entry' in data:
        entry =  data['entry']

    if 'tp1' in data:
        tp1 =  data['tp1']

    if 'tp2' in data:
        tp2 =  data['tp2']

    if 'tp3' in data:
        tp3 =  data['tp3']

    if 'tp4' in data:
        tp4 =  data['tp4']

    if 'stop' in data:
        stop =  data['stop']

    message = "幣種: " + basecurrency + "\n方向: " + side + "\n進場價格: " + entry + "\n第一止盈價格: " + tp1 + "\n第二止盈價格: " + tp2 + "\n第三止盈價格: " + tp3 + "\n第四止盈價格: " + tp4 + "\n止損價格: " + stop
    telegram_message(message)
    return jsonify({"status": "success", "message": request.json})
