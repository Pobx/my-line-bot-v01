from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('jK8m7axlXOnxkUkdG8uc6JxrhAzfLnD9mtPL7QqS4d83d3yb/9Em8anXpR/VZsnsjYbpF97qfOOslMt5ClX2HWTw27dSTTldd3P2iNjSPbBJC+bRuYST0rlIFcj3dl11VCG3tCZcQWfCbXlQV7ljJQdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('2c486f6c75ec8fd174ddb60c1daf21e9')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
