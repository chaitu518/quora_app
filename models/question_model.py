from config.db import questions_collection
from bson import ObjectId

async def create_question(data):
    result = await questions_collection.insert_one(data)
    return str(result.inserted_id)

async def get_all_questions():
    cursor = questions_collection.find()
    return [q async for q in cursor]

async def get_question_by_id(qid):
    return await questions_collection.find_one({"_id": ObjectId(qid)})