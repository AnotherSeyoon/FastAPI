from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the curent user"}

@app.get("/users/{item_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}