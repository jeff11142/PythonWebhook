from flask import Flask, request, jsonify
import requests

def telegram_message(request):
    data = request.json

    url = "https://api.telegram.org/bot5570850767:AAG1ucj0OECjbfaWVcAYZKiKzI4AnUEwy04/sendMessage?chat_id=@jeffliu_trading_alert&text=test"
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        print("TG訊息傳送成功")
        data = response.json()  # 解析 JSON 响应数据
        print(data)
        return "TG訊息傳送成功"

    else:
        print("TG訊息傳送失敗:", response.status_code)
        return "TG訊息傳送失敗"
