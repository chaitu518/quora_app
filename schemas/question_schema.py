from pydantic import BaseModel
from typing import List

class QuestionCreate(BaseModel):
    title: str
    description: str
    user_id: str

class QuestionOut(BaseModel):
    id: str
    title: str
    description: str
    user_id: str
    answers: List = []