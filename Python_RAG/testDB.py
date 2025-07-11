# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv

# load_dotenv()
# uri = os.getenv("MONGO_URI")
# print("your uri is", uri)
# client = MongoClient(uri)
# try:
#     client.admin.command('ping')
#     print("✅ Successfully connected to MongoDB!")
# except Exception as e:
#     print("❌ Failed to connect:", e)


m = "I like to play tennis"
d = m.split()
print(d)