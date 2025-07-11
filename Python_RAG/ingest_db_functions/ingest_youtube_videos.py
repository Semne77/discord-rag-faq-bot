from pydoc import text
from pymongo import MongoClient
import voyageai
import os
from typing import Any, Dict,List
# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["youtube_bot"]
collection = db["youtube_videos"]

# Initialize embedding client
voyage_client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

def delete_all_documents():
    result = collection.delete_many({})
    print(f"✅ Deleted {result.deleted_count} documents from the collection.")

# # Example video data
# video: Dict[str, Any] = {
#     "title": "Transformers Explained Visually",
#     "description": "This video explains transformer architecture for NLP.",
#     "link": "https://www.youtube.com/watch?v=abc123"
# }
videos: List[Dict[str, Any]]  =  [
    {
        "title": "Training for AI Engineers",
        "description": "Google Doc: Structured resource for engineers learning AI.",
        "link": "https://docs.google.com/document/d/1NfmEDyxrJ7Tz7Wq4IAJHx1fQ4bPpM5v07dPTM4pjOsM/edit?tab=t.0"
    },
    {
        "title": "Training of AI Designer",
        "description": "Google Doc: Resource guide for AI designers.",
        "link": "https://docs.google.com/document/d/1GkGijGY1jLPrmm-MSRYoCj3FTJwWB_RxlgapRMF6Eg0/edit?tab=t.0"
    },
    {
        "title": "Google Ranking form for engineers",
        "description": "Google Form for engineers ranking AI resources.",
        "link": "https://docs.google.com/forms/d/e/1FAlpQLSeMIdZwHGNcvJcF-e-jPW4bepNL_OnBmbB4w-s58HUNEW1kkg/viewform"
    },
    {
        "title": "The Illustrated Transformer",
        "description": "Jay Alammar's illustrated guide to the Transformer architecture.",
        "link": "https://jalammar.github.io/illustrated-transformer/"
    },
    {
        "title": "Neural Networks: Zero to Hero",
        "description": "YouTube playlist by Andrej Karpathy on neural networks.",
        "link": "https://www.youtube.com/playlist?list=PLAIqh1ijxbuWI23v9cThsA9GvCAUhRvKZ"
    },
    {
        "title": "Introduction - Hugging Face NLP Course",
        "description": "Hugging Face LLM course introduction chapter.",
        "link": "https://huggingface.co/learn/llm-course/chapter1/1"
    },
    {
        "title": "Generative AI for Beginners | Microsoft Learn",
        "description": "Microsoft Learn series introducing generative AI for beginners.",
        "link": "https://learn.microsoft.com/en-us/shows/generative-ai-for-beginners/"
    },
    {
        "title": "What is a Vector Database & How Does it Work?",
        "description": "Pinecone guide to understanding vector databases.",
        "link": "https://www.pinecone.io/learn/vector-database/"
    },
    {
        "title": "OpenAI Cookbook on GitHub",
        "description": "Collection of example OpenAI use cases and code snippets.",
        "link": "https://github.com/openai/openai-cookbook"
    },
    {
        "title": "MLOps Zoomcamp by DataTalksClub",
        "description": "Free MLOps course by DataTalksClub on GitHub.",
        "link": "https://github.com/DataTalksClub/mlops-zoomcamp"
    },
    {
        "title": "FastAPI",
        "description": "Official documentation for FastAPI framework.",
        "link": "https://fastapi.tiangolo.com/"
    },
    {
        "title": "Docker For Data Scientists",
        "description": "YouTube video on using Docker in data science workflows.",
        "link": "https://www.youtube.com/watch?v=0qG_0CPQhpg"
    },
    {
        "title": "What Is Agile Methodology?",
        "description": "Introduction to Agile Methodology on YouTube.",
        "link": "https://www.youtube.com/watch?v=8eVXTyIZ1Hs"
    },
    {
        "title": "What Is Agile Scrum Framework?",
        "description": "Overview of Scrum within Agile frameworks.",
        "link": "https://www.youtube.com/watch?v=B7VucspZA68"
    },
    {
        "title": "Master the Daily Scrum: Everything You Need to Know",
        "description": "Comprehensive guide to the daily Scrum process.",
        "link": "https://www.youtube.com/watch?v=xcCOLmkzG9g"
    },
    {
        "title": "Project team match video on YouTube",
        "description": "Example video for matching project teams.",
        "link": "https://www.youtube.com/watch?v=74CNxLh1dXY"
    },
    {
        "title": "Advanced Prompting Techniques",
        "description": "Prompting Guide covering advanced prompt engineering techniques.",
        "link": "https://www.promptingguide.ai/techniques"
    },
    {
        "title": "Langchain agents simply explained",
        "description": "Quick explanation of Langchain agents on YouTube.",
        "link": "https://youtu.be/Xi9Ui-9qcPw"
    },
    {
        "title": "Machine Learning Master",
        "description": "Website offering practical machine learning tutorials.",
        "link": "https://machinelearningmastery.com/"
    },
    {
        "title": "Underfitting & Overfitting - Explained",
        "description": "YouTube video explaining underfitting and overfitting in ML.",
        "link": "https://youtu.be/o3DztvnfAJg"
    },
    {
        "title": "Machine Learning Fundamentals: Bias and Variance",
        "description": "Explains bias and variance in machine learning.",
        "link": "https://youtu.be/EuBBz3bI-aA"
    },
    {
        "title": "What is MLOps?",
        "description": "YouTube video introducing MLOps concepts.",
        "link": "https://youtu.be/OejCJL2EC3k"
    },
    {
        "title": "What is Feature Engineering?",
        "description": "Video explaining feature engineering in ML workflows.",
        "link": "https://youtu.be/AnZWCB1gpFE"
    },
    {
        "title": "Parameters vs hyperparameters in machine learning",
        "description": "Explains the difference between parameters and hyperparameters.",
        "link": "https://youtu.be/V4AcLJ2cgmU"
    },
    {
        "title": "Machine Learning Model Deployment Explained",
        "description": "Guide to deploying machine learning models.",
        "link": "https://youtu.be/SHyFjJ-tlJE"
    },
    {
        "title": "Data cleaning in production time",
        "description": "Practical guide to cleaning data during production pipelines.",
        "link": "https://youtu.be/P8ERBy91Y90?si=yZ37-ScTbjtK4Af"
    },
    {
        "title": "Image classification vs Object detection vs Image Segmentation",
        "description": "Comparison of different computer vision tasks.",
        "link": "https://youtu.be/taC5pMCm70U"
    },
    {
        "title": "Unsupervised: Clustering, Dimensionality Reduction",
        "description": "Explains unsupervised learning methods.",
        "link": "https://youtu.be/AU_hBML2H1c"
    },
    {
        "title": "Reinforcement Learning",
        "description": "Explains the fundamentals of reinforcement learning.",
        "link": "https://youtu.be/Lu56xVIZ40M"
    },
    {
        "title": "Generative Models",
        "description": "Explains generative models and their applications.",
        "link": "https://youtu.be/TpMIssRdhco"
    },
    {
        "title": "Model Distillation",
        "description": "Overview of model distillation techniques.",
        "link": "https://youtu.be/zjaz2mC1KhM"
    },
    {
        "title": "Self-hosting LLMs",
        "description": "All you need to know about running LLMs locally.",
        "link": "https://youtu.be/XwL_cRuXM2E?si=vtmA2i40VMhZiBuN"
    },
    {
        "title": "Agentic Design Patterns Part 1",
        "description": "DeepLearning.ai article on agentic design patterns for LLMs.",
        "link": "https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/"
    },
    {
        "title": "Reflection Agents example",
        "description": "YouTube example on reflection agents.",
        "link": "https://www.youtube.com/watch?v=v5ymBTXNqtk"
    },
    {
        "title": "Multi-agent Collaboration",
        "description": "DeepLearning.ai article on multi-agent collaboration patterns.",
        "link": "https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration"
    },
    {
        "title": "LangGraph: Agent Evaluations",
        "description": "YouTube video on LangGraph agent evaluations.",
        "link": "https://www.youtube.com/watch?v=_QozKR9eQE8"
    }
    ,
    {
        "title": "Learn SQL in 1 hour",
        "description": "Fast-paced SQL tutorial for beginners.",
        "link": "https://www.youtube.com/watch?v=HXV3zeQKqGY"
    },
    {
        "title": "Database design tutorial",
        "description": "Tutorial on designing databases for structured data storage.",
        "link": "https://www.youtube.com/watch?v=ztHopE5Wnpc"
    },
    {
        "title": "Database schema",
        "description": "Explains the concept and structure of database schemas.",
        "link": "https://www.youtube.com/watch?v=ztHopE5Wnpc"
    },
    {
        "title": "Logical Database Design and E-R Diagrams",
        "description": "Covers logical database design and creating Entity-Relationship diagrams.",
        "link": "https://www.youtube.com/watch?v=QpdhBUYk7Kk"
    },
    {
        "title": "Python for beginners",
        "description": "Full Python programming course for beginners (4 hours).",
        "link": "https://www.youtube.com/watch?v=_uQrJ0TkZlc"
    },
    {
        "title": "Python Library for Data Science",
        "description": "Introduction to using Pandas and NumPy for data manipulation in Python.",
        "link": "https://www.youtube.com/watch?v=vmEHCJofslg"
    },
    {
        "title": "Python database Connection",
        "description": "Explains connecting Python to SQL databases using libraries like SQLAlchemy.",
        "link": "https://www.youtube.com/watch?v=5r4GZDtyBz0"
    },
    {
        "title": "SQL database with Pandas and Python",
        "description": "Tutorial on interacting with SQL databases using Pandas and Python.",
        "link": "https://www.youtube.com/watch?v=4C6I-BcK2nY"
    }
]

# Generate text for embedding
text_for_embedding = [video["title"] + ". " + video["description"] for video in videos]

# Get embeddings for all videos
embeddings = voyage_client.embed(
    text_for_embedding, 
    model="voyage-large-2", 
    input_type="document"
).embeddings

# Assign each embedding to the corresponding video and insert into MongoDB
for i in range(len(videos)):
    videos[i]["embedding"] = embeddings[i]
    result=collection.insert_one(videos[i])
    print(f"Inserted video with _id: {result.inserted_id}")


