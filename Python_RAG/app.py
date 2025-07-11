import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_services import generate_embedding, generate_answer_together
from youtube_videos import handle_question
from db import insert_document, vector_search
import uvicorn
import os
from ingest_db_functions.ingest_bootcamp_journey import chunk_text

app = FastAPI()

class IngestRequest(BaseModel):
    document: str

class QueryRequest(BaseModel):
    query: str

class YouTubeQueryRequest(BaseModel):
    query: str


@app.post("/ingest")
async def ingest_document(req: IngestRequest):
    try:
        listOfChunks = chunk_text(req.document)
        for i in listOfChunks:
            embedding = generate_embedding(i)
            insert_document({"document": i, "embedding": embedding})
        print("the ammount of chunks were generated are", len(listOfChunks))
        return {"message": "Document ingested successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag-query")
async def rag_query(req: QueryRequest):
    try:
        print("start of API")
        query_embedding = generate_embedding(req.query)
        print("imput embeded")
        results = vector_search(query_embedding)
        print("vector_search results:", results)

        context = "\n".join([doc.get("document", "") for doc in results])
        answer = generate_answer_together(req.query, context)
        return {"answer": answer, "chunks": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag-youtube-query")
async def rag_youtube_query(req: YouTubeQueryRequest):
    try:
        print(f"Received query: {req.query}")
        answer = handle_question(req.query)
        print(f"Generated answer: {answer}")
        return {"answer": answer}
    except Exception as e:
        import traceback
        print(f"Error in /rag-youtube-query: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
