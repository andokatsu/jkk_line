import requests

# LINE Notifyの設定
LINE_NOTIFY_TOKEN = 'r5GKKGRwPlFqPKO5PLsnjQ5qgoTg9U57wGB2cr1Bzot'
LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'

def line(message):
    """LINE Notifyでメッセージを送信"""
    headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
    data = {'message': message}
    response = requests.post(LINE_NOTIFY_API, headers=headers, data=data)
    if response.status_code == 200:
        print('LINE通知を送信しました。')
    else:
        print(f'LINE通知の送信に失敗しました。ステータスコード: {response.status_code}')