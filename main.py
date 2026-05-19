from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get('/items/{item_id}')
async def read_items(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Dynamic Route
@app.get("/users/{user_id}")
async def get_user(user_id:int):
    return {"user_id": user_id}