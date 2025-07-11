import voyageai
import os
from dotenv import load_dotenv
from together import Together

load_dotenv()

# VoyageAI client for embeddings
voyage_client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

# Together AI client for generation
together_client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def generate_embedding(text):
    """
    Generate embeddings using VoyageAI for semantic search.
    """
    if not text.strip():
        raise ValueError("Empty text for embedding.")
    embedding = voyage_client.embed(text, model="voyage-large-2", input_type="document")
    return embedding.embeddings[0]

def generate_answer_together(question, context):
    """
    Generate an answer using Together AI (DeepSeek-V3 or your chosen model).
    """
    response = together_client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",   # adjust model here if desired
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Use the provided context to answer the user's question accurately and concisely."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ]
    )
    return response.choices[0].message.content
