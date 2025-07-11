from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["knowledge"]
collection = db["research_papers"]

def insert_document(doc):
    collection.insert_one(doc)

def vector_search(query_embedding, limit=5):
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 150,
                "limit": limit
            }
        },
        {
            "$project": {
                "_id": 0,
                "embedding": 0,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]
    return list(collection.aggregate(pipeline))


