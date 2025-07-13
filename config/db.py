from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://saichaitanya518:bldvTzNqfDpeHpzw@cluster0.aigkqx1.mongodb.net/")
db = client.quora

questions_collection = db.questions
answers_collection = db.answers
