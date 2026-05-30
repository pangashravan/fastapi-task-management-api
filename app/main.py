from fastapi import FastAPI

app = FastAPI(title="Task Management API")

@app.get("/")
async def root():
    return {"message": "API running"}
