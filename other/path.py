import os
import json

path = "Python"
# 取得Python目錄下的Username目錄
file_list = os.listdir(path)
print(file_list)
userlist = file_list
# 取得username目錄下的repoName
i=0
data = {}
for user in userlist:
    repo_list = os.listdir(path+"/"+user)
    print(repo_list)
    
    
    for repo in repo_list:
        nowpath = path+"/"+user+"/"+repo
        i+=1
        data[i] = nowpath
                    
with open("table.json", "w") as f:
    json.dump(data, f)