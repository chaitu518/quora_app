from fastapi import APIRouter
from utils.serilizer import serialize_question
from schemas.question_schema import QuestionCreate,QuestionOut
from models import question_model
router = APIRouter()

@router.post("/",response_model=QuestionOut)
async def get_questions(q:QuestionCreate):
    qid = await question_model.create_question(q.dict())
    return {**q.dict(), "id": qid, "answers": []}

@router.get("/", response_model=list[QuestionOut])
async def list_all():
    questions = await question_model.get_all_questions()
    response = []
    for q in questions:
        response.append({
            **serialize_question(q),
            "answers": []
        })
    return response