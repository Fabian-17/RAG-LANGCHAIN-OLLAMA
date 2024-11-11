from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.chain import chain

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
async def query_endpoint(query: QueryRequest):
    try:
        response = chain.invoke(query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))