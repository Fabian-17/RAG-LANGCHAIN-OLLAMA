from fastapi import FastAPI, HTTPException
from api.endpoints import router

app = FastAPI(title="Chatbot RAG")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Chatbot con RAG"}