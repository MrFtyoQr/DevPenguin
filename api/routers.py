# api/routers.py
from fastapi import APIRouter, HTTPException
from services.openrouter_service import OpenRouterService

router = APIRouter()
service = OpenRouterService()

@router.post("/ask")
def ask_question(question: str):
    try:
        response = service.get_response(question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))