import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def getDayTrending():
    url = "https://github.com/trending/python?since=daily"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.content, "html.parser")
    repo_list = soup.find_all("h1", class_="h3 lh-condensed")

    # 获取当前日期并将其格式化为字符串
    date_str = datetime.now().strftime("%Y-%m-%d")

    folder_name = "Github_Trending_Daily"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    with open(f"Github_Trending_Daily/github_trending_{date_str}.html", "w", encoding="utf-8") as file:
        file.write(str(soup))
    return soup

def getWeeklyTrending():
    url = "https://github.com/trending/python?since=weekly"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.content, "html.parser")
    repo_list = soup.find_all("h1", class_="h3 lh-condensed")

    # 获取当前日期并将其格式化为字符串
    date_str = datetime.now().strftime("%Y-%m-%d")

    folder_name = "Github_Trending_Weekly"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    with open(f"Github_Trending_Weekly/github_trending_{date_str}.html", "w", encoding="utf-8") as file:
        file.write(str(soup))
    return soup
getDayTrending()
getWeeklyTrending()