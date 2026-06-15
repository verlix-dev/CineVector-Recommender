import hybrid_recommendation
from vector_recommendation import vector_movie_recommendation
from atlas_recommendation import atlas_movie_recommendation
from hybrid_recommendation import hybrid_movie_recommendation  






# vector_movie_recommendation("psychological thriller involving dreams")
# atlas_movie_recommendation("time travel movie")
hybrid_movie_recommendation("time travel movie")











# docs = list(
#     model_and_database.collection.find(
#         {
#             "plot": {"$exists": True},
#             "plot_embedding_hf_": {"$exists": False}
#         }
#     )
# )


# for doc in docs:
#     embedding = get_embedding(doc["plot"])

#     model_and_database.collection.update_one(
#         {"_id": doc["_id"]},
#         {"$set": {"plot_embedding_hf_": embedding}}
#     )

#     print("Updated:", doc["title"])