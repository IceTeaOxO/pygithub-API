# Github API
## Introduction
使用pygithub來獲取更客製化的github搜尋，並且加上github trending紀錄
## 使用方法
1. ```pip install requirements.txt```
2. 將.env.sample的名稱改為.env,並輸入自己的github api key
3. 在.env檔案中設定自己想要的搜尋條件，然後執行repo_crawler.py，取得符合搜尋條件的專案ID
4. 啟動detail.py取得專案的詳細資料，並將資料存入sqlite
5. 啟動API.py開啟server，在網址列輸入```http://127.0.0.1:8000/repos```即可獲取資料庫裡的資料
6. 提供兩種參數可調整回傳的結果`limit`限制回傳的資料數量`offset`指定從第幾筆資料開始回傳

## 取得github trending
1. 啟動timeTask.py，每隔1天會抓取一次github trending
2. 打開API.py，在網址列輸入`http://127.0.0.1:8000/trendingDaily`
## Corboration

【Git規則】
在做任何更動之前，確保是在自己的branch上（而不是main）改動
有任何main的改動統一由教學長大人負責

## File statement

【Python資料夾】
內部主要是爬蟲所爬下來的東西，不用往裡面看
【API.py】


【DB.py】

【detail.py】

【repo_crawler.py】

## 未解決問題
1. 增加github trending可以跳轉到不同日期的方法
2. 提供更好的系統設計方法，可以發pr