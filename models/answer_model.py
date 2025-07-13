from config.db import answers_collection
from bson import ObjectId

async def create_answer(data):
    result = await answers_collection.insert_one(data)
    return str(result.inserted_id)

async def get_answers_by_question(qid: ObjectId):
    return [a async for a in answers_collection.find({"question_id": qid})]