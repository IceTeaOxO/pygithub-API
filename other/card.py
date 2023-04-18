import json
with open("temp.html","r") as f:
    card = f.read()
with open("table.json","r") as f:
    table = json.load(f)
    
# print(card)
# print(table)

start = '<!DOCTYPE html><html><head><title>Github Card</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0" crossorigin="anonymous"></head><body>'
card = '<div class="card w-50" style="width: 18rem;"><div class="card-body">'
title = '<h5 class="card-title">'
titleend = "</h5>"
text  = '<p class="card-text">'
textend = "</p>"
cardend = '</div></div>'
end = "</body></html>"
p = "<p>"
a = '<a href="'
aa = '">'
aend = '</a>'

def make_html(authname,reponame,url,issues,stars):
    html = start+card+title+authname+"/"+reponame+titleend+text+p+"URL:"+a+url+aa+url+aend+p+"Stars:"+stars+p+"Issues:"+issues+textend+cardend+end
    return html

# print(len(table))
for i in range(len(table)):
    # print(table[str(i+1)])
    path = table[str(i+1)]
    with open(path+"/metadata.json","r") as fr:
        data = json.load(fr)
        authname = data["authname"]
        reponame = data["reponame"]
        url = data["URL"]
        issues = data["open_issues"]
        stars = data["stars"]
    with open("html/"+authname+"-"+reponame+".html","w") as f:
        html = make_html(authname,reponame,str(url),str(issues),str(stars))
        # print(stars)
        # print(issues)
        f.write(html)
