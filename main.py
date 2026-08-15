from fastapi import FastAPI

app = FastAPI()

@app.head("/")
@app.get("/")
async def index():
    return {
        "success": 1
    }

port='hi'
@app.get(f"/{port}/good")
async def index():
    return {
        "success": "vdhfns"
    }
