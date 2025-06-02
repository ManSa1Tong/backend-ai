from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "만사일통 AI 서버입니다."}
