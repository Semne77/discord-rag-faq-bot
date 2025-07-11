import voyageai
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from together import Together

load_dotenv()

# Initialize clients
voyage_client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))
together_client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

# MongoDB setup
mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client["youtube_bot"]
collection = db["youtube_videos"]

def generate_embedding(text):
    """
    Generate embeddings using VoyageAI for semantic search.
    """
    if not text.strip():
        raise ValueError("Empty text for embedding.")
    embedding = voyage_client.embed(text, model="voyage-large-2", input_type="document")
    return embedding.embeddings[0]

def vector_search(query_embedding, limit=5):
    """
    Vector search using MongoDB Atlas $vectorSearch.
    """
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
                "title": 1,
                "description": 1,
                "link": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]
    return list(collection.aggregate(pipeline))

def generate_answer_together(question, context, model="deepseek-ai/DeepSeek-V3", temperature=0.2, max_tokens=512):
    """
    Generate an answer using Together AI with retrieved context.

    Args:
        question (str): User's question.
        context (str): Context retrieved from vector DB.
        model (str): Together model name.
        temperature (float): Sampling temperature.
        max_tokens (int): Max tokens in output.

    Returns:
        str: The generated answer.
    """
    if not question.strip():
        return "⚠️ Please provide a question."

    if not context.strip():
        context = "No additional context provided."

    prompt = (
        "You are a helpful assistant. Use the provided context to answer the user's question accurately and concisely.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )

    try:
        response = together_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[TogetherAI Error] {e}")
        return "⚠️ Sorry, I was unable to generate an answer at this time."


def handle_question(question):
    """
    Main pipeline: embed -> vector search -> generate answer or return links.
    """
    question_embedding = generate_embedding(question)
    top_videos = vector_search(question_embedding, limit=3)
    print("This is the retrieved from the database 3 chunks", top_videos)

    # Format context for LLM
    context = ""
    for idx, vid in enumerate(top_videos, 1):
        context += (
            f"Video {idx}:\n"
            f"Title: {vid['title']}\n"
            f"Description: {vid['description']}\n"
            f"Link: {vid['link']}\n\n"
        )

    # If user explicitly asks for links, return them directly
    if any(keyword in question.lower() for keyword in ["link", "video", "watch", "youtube", "resources"]):
        links_response = "Here are some relevant videos you can watch:\n\n"
        for vid in top_videos:
            links_response += f"- {vid['title']}: {vid['link']}\n"
        return links_response

    # Otherwise, generate an answer
    return generate_answer_together(question, context)


