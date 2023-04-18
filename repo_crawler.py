from dotenv import load_dotenv
import os
import time
from github import Github, GithubException

# 加載.env文件中的環境變數
load_dotenv()

# 使用os.getenv()方法獲取環境變數
key = os.getenv("github_key")
g = Github(key)
query = os.getenv("query")
order = os.getenv("order")
sort = os.getenv("repo_sort")
qf = os.getenv("repo_qf")
#讀取環境變數，設定搜尋條件
query = query+" "+qf
print(query,order,sort)

try:
    repos = g.search_repositories(query=query,order=order,sort=sort)

    for repo in repos:
        #將符合查詢結果的資料存入repo.md
        with open('repo.md', 'a') as f:
            f.write(repo.owner.login+"/"+repo.name+"\n"+str(repo.id)+"\n")
        with open('repoID.md', 'a') as f:
            f.write(str(repo.id)+"\n")
            
except GithubException as e:
    # 配額超限異常，等待配額重置後再繼續使用 API
    reset_time = g.rate_limiting_resettime
    print(f"Rate limit exceeded. Waiting until {reset_time}...")
    time.sleep(reset_time - time.time())
        
    # print(repo.html_url)
    # print(repo.open_issues)#有多少open issues
    # # print(repo.contributors_url)#可以用來額外追蹤
    # print(repo.language)
    # print(repo.topics)#可以用來額外追蹤
    # print(repo.size)#判斷大小