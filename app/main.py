# app/main.py
from fastapi import FastAPI
from app.api.routes import api_router

app = FastAPI()

# Include the API routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Oil Spill Detection System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
