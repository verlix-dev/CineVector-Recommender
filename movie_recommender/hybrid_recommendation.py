import model_and_database
from embedding import get_embedding

def hybrid_movie_recommendation(query: str):
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

    vector_results = model_and_database.collection.aggregate(
        [
            {
                "$vectorSearch": {
                    "queryVector": query_embedding,
                    "path": "movie_embedding_v2",
                    "numCandidates": 200,
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

    atlas_results = model_and_database.collection.aggregate([
        {
            "$search": {
                "index": "atlas_search",
                "compound": {
                    "should": [
                        {
                            "text": {
                                "query": query,
                                "path": "title",
                                "score": {
                                    "boost": {
                                        "value": 3
                                    }
                                }
                            }
                        },
                        {
                            "text": {
                                "query": query,
                                "path": ["plot", "fullplot", "genres"]
                            }
                        }
                    ]
                }
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
                "score": {"$meta": "searchScore"}
            }
        },
        {
            "$limit": 20
        }
    ])
    movie_results = {}


    for result in atlas_results:
        result['atlas_score'] = result.pop('score', 0)

        movie_id = str(result["_id"])

        movie_results[movie_id] = result

    for result in vector_results:
        result['vector_score'] = result.pop('score', 0)

        movie_id = str(result["_id"])

        if movie_id in movie_results:
            movie_results[movie_id].update(result)
        else:
            movie_results[movie_id] = result     

    max_atlas = max(
        movie.get("atlas_score", 0)
        for movie in movie_results.values()
    )

    max_vector = max(
        movie.get("vector_score", 0)
        for movie in movie_results.values()
    )   
    for movie in movie_results.values():

        atlas = movie.get("atlas_score", 0)
        vector = movie.get("vector_score", 0)

        atlas_norm = atlas / max_atlas if max_atlas else 0
        vector_norm = vector / max_vector if max_vector else 0

        movie["final_score"] = (
            0.4 * atlas_norm +
            0.4 * vector_norm +
            0.2 * min(atlas_norm, vector_norm)
        )


    results = sorted(
        movie_results.values(),
        key=lambda x: x.get("final_score",0),
        reverse=True
    )
    print("Unique movies:", len(movie_results))

    recommendations = []

    for movie in results[:10]:
        recommendations.append({
            "title": movie.get("title"),
            "poster": movie.get("poster"),
            "genres": movie.get("genres"),
            "year": movie.get("year"),
            "plot": movie.get("plot"),
            "score": round(movie.get("final_score", 0), 3)
        })

    return recommendations
    # seen = set()
    # for result in movie_results.values():
    #     if result.get('title') in seen:
    #         continue
    #     seen.add(result.get('title'))
    #     combined_text = f"""
    #         Title: {result.get('title','')}
    #         Genres: {' '.join(result.get('genres', []))}  
    #         Year: {result.get('year','')}
    #         Directors: {' '.join(result.get('directors', []))}
    #         Plot: {result.get('plot','')}
    #         Search Score: {result.get('score', 0):.4f}
    #         Vector Score: {result.get('vector_score', 0):.4f}
    #         """
    #     print(combined_text)
