from fastapi import FastAPI
from controllers import question_controller, answer_controller

app = FastAPI()

app.include_router(question_controller.router, prefix="/questions", tags=["Questions"])
app.include_router(answer_controller.router, prefix="/answers", tags=["Answers"])