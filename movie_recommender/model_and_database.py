from pydoc import doc

import pymongo # type: ignore
import requests # type: ignore
from sentence_transformers import SentenceTransformer # type: ignore

client = pymongo.MongoClient("")#add the mongodb connection here
db = client.sample_mflix
collection = db.movies

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

