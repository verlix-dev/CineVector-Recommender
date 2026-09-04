from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import model_and_database # type: ignore
from vector_recommendation import vector_movie_recommendation
from atlas_recommendation import atlas_movie_recommendation
from hybrid_recommendation import hybrid_movie_recommendation  


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}


@app.get("/recommend/vector")
def recommend_vector(query: str):
    return vector_movie_recommendation(query)




@app.get("/recommend/atlas")
def recommend_atlas(query: str):
    return atlas_movie_recommendation(query)
    


@app.get("/recommend/hybrid")
def recommend_hybrid(query: str):
    return hybrid_movie_recommendation(query)
    
