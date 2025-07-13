
def serialize_question(q):
    return {
        "id": str(q["_id"]),
        "title": q["title"],
        "description": q["description"],
        "user_id": q["user_id"]
    }
def serialize_answer(a):
    return {
        "id": str(a["_id"]),
        "question_id": str(a["question_id"]),
        "user_id": a["user_id"],
        "content": a["content"],
        "sentiment": a["sentiment"]
    }