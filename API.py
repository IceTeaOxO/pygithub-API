from fastapi import FastAPI,Response
from fastapi.responses import FileResponse,HTMLResponse
import os
import json
import DB
from fastapi.middleware.cors import CORSMiddleware
import Trending

app = FastAPI()

#解決CORS問題
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

#這裡提供查詢服務，可以透過特定請求來獲得特定排列的結果
@app.get("/repos")
async def repos(limit=10,offset=0):
    db = DB.GithubDB('github.db')
    result = db.select_data('github',limit=limit,offset=offset)
    json_result = json.dumps(result)
    return Response(content=json_result, media_type="application/json")
@app.get("/trendingDaily")
async def trending_daily():
    data = Trending.getDayTrending()
    return HTMLResponse(content=data, status_code=200)
@app.get("/trendingWeekly")
async def trending_weekly():
    data = Trending.getWeeklyTrending()
    return HTMLResponse(content=data, status_code=200)

@app.get("/issues")
async def issues():
    return ""

@app.get("/python")
async def python():
    return ""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
#uvicorn API:app --reload
