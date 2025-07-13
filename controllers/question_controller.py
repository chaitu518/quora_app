from fastapi import APIRouter
from utils.serilizer import serialize_question,serialize_answer
from schemas.question_schema import QuestionCreate,QuestionOut
from models import question_model,answer_model
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
        answers = await answer_model.get_answers_by_question(q["_id"])
        response.append({
            **serialize_question(q),
            "answers": [serialize_answer(a) for a in answers]
        })
    return response