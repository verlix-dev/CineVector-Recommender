from pydoc import doc

import pymongo
import requests
from sentence_transformers import SentenceTransformer

client = pymongo.MongoClient("mongodb+srv://priyanshu17900_db_user:5lSPe5NNauWawlEH@cluster0.ew5enq2.mongodb.net/?appName=Cluster0")
db = client.sample_mflix
collection = db.movies

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

