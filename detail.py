import os
from dotenv import load_dotenv
from github import Github, GithubException
import json
import DB
import datetime
today = datetime.date.today()
# 加載.env文件中的環境變數
load_dotenv()

# 使用os.getenv()方法獲取環境變數
key = os.getenv("github_key")
g = Github(key)

#將資料存入資料庫
my_db = DB.GithubDB('github.db')
my_db.create_table("github")
insert_data = []

with open("repoID.md", "r") as fr:
    # 讀取檔案內容
    # content = f.read()
    line = fr.readline()
    #還有下一行文字就會執行迴圈
    while line:
        linedata = []
        repoID = int(line)
        repo = g.get_repo(repoID)
        # print(repo.name)
        # print(repo.language)
        readme_contents =repo.get_readme().decoded_content

        # 要寫入的檔案路徑
        file_path = repo.language+"/"+repo.owner.login+"/"+repo.name+"/dir.txt"
        # 檢查目錄是否存在，如果不存在，創建該目錄
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        #寫入readme.md
        with open(repo.language+"/"+repo.owner.login+"/"+repo.name+"/"+"README.md", "wb") as f:
            f.write(readme_contents)
            
        linedata.extend([repo.owner.login,repo.name,repo.html_url,int(repo.open_issues),int(repo.stargazers_count),str(today),repo.language+"/"+repo.owner.login+"/"+repo.name+"/"+"README.md",repo.language])
        insert_data.append(linedata)
        
        #插入資料
        my_db.insert_data(insert_data)

        insert_data = []
        
        line = fr.readline()



print("completed!")


#寫入metadata.json，URL,open issues,topic,stars
        # with open(repo.language+"/"+repo.owner.login+"/"+repo.name+"/"+"metadata.json", "w") as f:
        #     data = {"authname":repo.owner.login,"reponame":repo.name,"URL":repo.html_url, "open_issues":str(repo.open_issues), "topics":repo.topics, "stars":str(repo.stargazers_count)}
        #     json.dump(data, f)