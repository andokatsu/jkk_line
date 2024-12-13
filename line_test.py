import requests

def line(str,num):
    if num == 0:
        line_notify_token = 'r5GKKGRwPlFqPKO5PLsnjQ5qgoTg9U57wGB2cr1Bzot'
    if num == 1:
        line_notify_token = 'r5GKKGRwPlFqPKO5PLsnjQ5qgoTg9U57wGB2cr1Bzot'
    
    #テンプレ
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = '\n' + str
    payload = {'message':message}
    headers = {'Authorization': 'Bearer ' + line_notify_token} 
    line_notify = requests.post(line_notify_api,data=payload,headers=headers)
    
str = 'テスト送信'
num = 0

#実行
line(str,num)