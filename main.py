from fastapi import FastAPI

app = FastAPI()

@app.head("/")
@app.get("/")
async def index():
    return {
        "success": 1
    }
