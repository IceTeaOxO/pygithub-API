import schedule
import time
import Trending
def dailyJob():
    Trending.getDayTrending()
def weeklyJob():
    Trending.getWeeklyTrending()

# 每隔86400秒钟执行一次job函数
schedule.every(86400).seconds.do(dailyJob)
schedule.every(7).days.do(weeklyJob)

while True:
    #不断检查定时任务是否到期，并执行需要执行的任务。
    schedule.run_pending()
    time.sleep(3600)