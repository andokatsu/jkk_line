#スクリプトを定期実行するためにscheduleをインポート
import schedule
import time
import Property_search

# 1時間ごとに関数を実行するスケジュールを設定
Property_search.property_search(schedule.every(1).hours.do())

# スケジュールを処理
print("定期実行を開始します...")
while True: # while True: →　無限ループを作成。このループ内でスケジュールを常に監視する。
    schedule.run_pending() # schedule.run_pending(): →　現在のスケジュールの中で、実行が予定されているタスクを確認し、該当するものを実行。
    time.sleep(1) # 1秒間待機してからループを再度実行。CPU負荷を軽減するための処理で、スケジュールが空回りしないように短い休止時間を設定している。