from voyageai.client import Client
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("VOYAGE_API_KEY")
client = Client(api_key=api_key)

def test_embedding(text):
    embedding = client.embed(text, model="voyage-large-2", input_type="document")
    print("✅ Embedding generated successfully!")
    print(embedding.embeddings[0])

if __name__ == "__main__":
    test_embedding("This is a test sentence for embedding.")
