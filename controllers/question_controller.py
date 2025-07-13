from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def get_questions():
    return {
        "q":"hello guys"
    }