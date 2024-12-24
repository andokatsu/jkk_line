#実行環境(2024/12/13時点)
#Python 3.11.8
#ChromeDriver 126.0.6478.55
#selenium  4.18.1

import time
import line_test

#自動的にChromeDriverのバージョンをブラウザのバージョンと一致させる
#webdriver-managerは各ブラウザのバージョンを自動で確認して実行してくれるライブラリ
#ブラウザのバージョンアップの度にドライバを用意するという手間が省ける
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#By関数を使用するため、Byをインポート
from selenium.webdriver.common.by import By
#WebDriverWaitをインポート
from selenium.webdriver.support.ui import WebDriverWait
#expected_conditionsで状態変化を調べる
from selenium.webdriver.support import expected_conditions as EC


#港区の空き部屋情報をチェック
def check_vacancies():
    
    # Seleniumの設定
    options = Options()
    options.add_argument("--headless")  # ヘッドレスモードで実行→Chrome ヘッドレス モードを使用すると、
    #UI を表示せずに無人環境でブラウザを実行できます。つまり、Chrome なしで Chrome を実行できます。
    options.add_argument("--disable-dev-shm-usage") # ディスクのメモリスペースを使う。DockerやGcloudのメモリ対策でよく使われる。
    #下記2行は不要/ソース→ https://qiita.com/kawagoe6884/items/cea239681bdcffe31828
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    
    #pip install chromedriver-binary-autoをターミナル(cmdで実行したため下記は不要な認識)
    #service = Service('/path/to/chromedriver')  # Chromedriverのパス
    
                                                
#待機時間を設定(対象が見つからなかったら再度探す時間)=暗黙的な待機
driver.implicitly_wait(10)
#スクレイピング対象HPを指定
driver.get('https://jhomes.to-kousya.or.jp/search/jkknet/service/akiyaJyoukenStartInit')
#HTMLのタブで括られたオブジェクト指定して探すために、find_elementというメソッドを使用
element = driver.find_element(By.LINK_TEXT, "こちら")
element.click()

 # 新しいタブに切り替え
driver.switch_to.window(driver.window_handles[-1])  # 最新のタブに切り替え

 # 対象エリアのチェックボックスを選択
target_areas = ["港区", "渋谷区", "中央区", "目黒区","中野区","杉並区","中央区","新宿区","文京区"]
for area in target_areas:
    checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{area}')]/preceding-sibling::input")
    if not checkbox.is_selected():
        checkbox.click()
        print(f"{area} のチェックボックスを選択しました。")
        time.sleep(0.5)  # チェック間に少し待機
        
# 駅までの所要時間を設定
#station_time = "5分以内" 
station = "10分以内" 
#station_time = "15分以内" 

# 駅までの所要時間を選択
radio_button = driver.find_element(By.XPATH, f"//label[contains(text(), '{station}')]/preceding-sibling::input")
radio_button.click()
print(f"駅までの所要時間を「{station}」に設定しました。")

# 「検索する」ボタンをクリック
search_button = driver.find_element(By.XPATH, "/html/body/div/table[1]/tbody/tr[2]/td/form/table/tbody/tr[5]/td/table/tbody/tr[3]/td/a/img")
search_button.click()
print("検索ボタンをクリックしました。")

# 結果が表示されるまで待機
driver.implicitly_wait(5)

if driver.find_elements(By.XPATH,"/html/body/div/table[1]/tbody/tr[2]/td/form/table/tbody/tr[4]/td/ul/li"):
    print("空き部屋は見つかりませんでした。")
    
elif driver.find_elements(By.XPATH,"/html/body/div/table[1]/tbody/tr[2]/td/form/table/tbody/tr[7]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/strong"):

    x = driver.find_element(By.XPATH,"/html/body/div/table[1]/tbody/tr[2]/td/form/table/tbody/tr[11]/td/table")   
    a = len(x.find_elements(By.TAG_NAME,"tr"))-1
    
    message = f'指定エリア（港区、渋谷区、中央区、目黒区、中野区、杉並区、中央区、新宿区、文京区）で {a}件の空き部屋があります！'
    print(message)
    line_test.line(message)
else:
    print("1件空き部屋が見つかりました")