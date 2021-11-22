from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextSendMessage,TextMessage
from linebot.models.messages import ImageMessage
import pymysql
host = '127.0.0.1'
port = 3306
user = 'ting'
passwd = '123456'
db = 'Store'
charset = 'utf8mb4'
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = conn.cursor()

app = Flask(__name__)
line_bot_api = LineBotApi('Ny82hBhe9IA01Hn+RiRXm1WxSue/bek32fMsVDa4CMmN6FfwFnt1uS9bAUaucrTJztE8Zed1XiF3egh4L08gj/zdqyvJwGzBUz+vOLtGESQxomnaApceuamV+Iz/vEk+3bfHwAJcfC1vrim7S9fksAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3c681c6ba63968861d6f13f5279ebde8')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    print('msg from [', user_name, '](', user_id, ') : ', msg)
    store = []
    city= []
    dist=[]
    if msg == '全家':
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入查詢縣市?'))
        store.append('familymart')
    if msg == '7-11':
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入查詢縣市?'))
        store.append('seveneleven')
    if (len(store)== 0) :
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請輸入商店'))
    citylist = ['台北市', '基隆市', '新北市', '桃園市', '新竹市', '台中市', '嘉義市', '台南市', '高雄市', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '宜蘭縣',
                '花蓮縣', '雲林縣', '嘉義縣', '台東縣', '屏東縣', '澎湖縣', '金門縣', '連江縣']
    if (msg in citylist) and (len(store)== 1) :
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入查詢區域?'))
        city.append(msg)
        print(len(store))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請重新輸入正確縣市'))

    sql = f"""
            SELECT dist
            from {store[0]}
            where city='{city[0]}';
            """
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in range(len(data)):
        c = data[i][0]
        dist.append(c)
    cursor.close()
    if msg in dist:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('是否街道查詢?請輸入是或否:'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('您輸入的區域沒有便利商店'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)