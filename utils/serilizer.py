
def serialize_question(q):
    return {
        "id": str(q["_id"]),
        "title": q["title"],
        "description": q["description"],
        "user_id": q["user_id"]
    }