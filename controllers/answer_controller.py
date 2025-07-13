from fastapi import APIRouter
from schemas.answer_schema import AnswerCreate, AnswerOut
from models import answer_model
from bson import ObjectId
from services import sentimental_service

router = APIRouter()

@router.post("/", response_model=AnswerOut)
async def create(a: AnswerCreate):
    sentiment_value = sentimental_service.analyze_sentiment(a.content)
    data = {
        "question_id": ObjectId(a.question_id),
        "user_id": a.user_id,
        "content": a.content,
        "sentiment": sentiment_value
    }
    aid = await answer_model.create_answer(data)
    return {
        "id": aid,
        "question_id": a.question_id,
        "user_id": a.user_id,
        "content": a.content,
        "sentiment": sentiment_value
    }
