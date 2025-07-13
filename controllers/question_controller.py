from fastapi import APIRouter
from utils.serilizer import serialize_question
from schemas.question_schema import QuestionCreate,QuestionOut
from models import question_model
router = APIRouter()

@router.post("/",response_model=QuestionOut)
async def get_questions(q:QuestionCreate):
    qid = await question_model.create_question(q.dict())
    return {**q.dict(), "id": qid, "answers": []}

