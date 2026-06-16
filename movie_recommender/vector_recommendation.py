import model_and_database
from embedding import get_embedding

def vector_movie_recommendation(query: str):
    query = query.lower()

    stop_words = {
        "movie",
        "film",
        "show",
        "films",
        "movies"
    }

    filtered_query = " ".join(
        word for word in query.split()
        if word not in stop_words
    )
    query = filtered_query
    query_embedding = get_embedding(query)

    results = model_and_database.collection.aggregate(
        [
            {
                "$vectorSearch": {
                    "queryVector": query_embedding,
                    "path": "movie_embedding_v2",
                    "numCandidates": 100,
                    "limit": 20,
                    
                    "index": "vector_index_v2"
                }
            },
            {
                "$project": {
                    "title": 1,
                    "poster": 1,
                    "plot": 1,
                    "genres": 1,
                    "year": 1,
                    "directors": 1,
                    "cast": 1,
                    "score": {"$meta": "vectorSearchScore"}
                }
            }
        ]
    )

    recommendations = []
    seen = set()

    for movie in results:

        title = movie.get("title")

        if title in seen:
            continue

        seen.add(title)

        recommendations.append({
            "title": title,
            "poster": movie.get("poster"),
            "genres": movie.get("genres"),
            "year": movie.get("year"),
            "plot": movie.get("plot"),
            "score": round(movie.get("score", 0), 3)
        })

        if len(recommendations) == 10:
            break

    return recommendations