#実行環境(2024/12/13時点)
#Python 3.11.8
#ChromeDriver 126.0.6478.55
#selenium  4.18.1

#自動的にChromeDriverのバージョンをブラウザのバージョンと一致させる
#webdriver-managerは各ブラウザのバージョンを自動で確認して実行してくれるライブラリ
#ブラウザのバージョンアップの度にドライバを用意するという手間が省ける
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#By関数を使用するため、Byをインポート
from selenium.webdriver.common.by import By
                                                
#待機時間を設定(対象が見つからなかったら再度探す時間)=暗黙的な待機
driver.implicitly_wait(10)
#スクレイピング対象HPを指定
driver.get('https://jhomes.to-kousya.or.jp/search/jkknet/service/akiyaJyoukenStartInit')
#HTMLのタブで括られたオブジェクト指定して探すために、find_elementというメソッドを使用
element = driver.find_element(By.LINK_TEXT, "こちら")
element.click()

element1 = driver.find_elements(By.CLASS_NAME, "cellFFFFFF")
print([s.text for s in element1])


# element_2 = driver.find_elements(By.ID, "ku")
# print([s.text for s in element_2])
