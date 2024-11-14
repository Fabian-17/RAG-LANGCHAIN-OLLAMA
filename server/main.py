from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router

app = FastAPI(title="Chatbot RAG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Chatbot con RAG"}