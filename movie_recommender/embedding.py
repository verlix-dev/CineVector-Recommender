import model_and_database


def get_embedding(text: str) -> list[float]:
    return model_and_database.model.encode(text).tolist()


docs = list(
    model_and_database.collection.find(
        {
            "plot": {"$exists": True},
            "movie_embedding_v2": {"$exists": False}
        }
    )
)