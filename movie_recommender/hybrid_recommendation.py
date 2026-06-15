import model_and_database
from embedding import get_embedding

def hybrid_movie_recommendation(query: str):
    query_embedding = get_embedding(query)

    vector_results = model_and_database.collection.aggregate(
        [
            {
                "$vectorSearch": {
                    "queryVector": query_embedding,
                    "path": "plot_embedding_hf_",
                    "numCandidates": 100,
                    "limit": 10,
                    
                    "index": "vector_index"
                }
            },
            {
                "$project": {
                    "title": 1,
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
                "text": {
                    "query": query,
                    "path": ["title", "plot", "fullplot", "genres"]
                }
            }
        },
        {
            "$project": {
                "title": 1,
                "plot": 1,
                "genres": 1,
                "year": 1,
                "directors": 1,
                "score": {"$meta": "searchScore"}
            }
        },
        {
            "$limit": 10
        }
    ])

    movie_results = {}


    for result in atlas_results:
        result['atlas_score'] = result.pop('score', 0)
        movie_results[result.get('title')] = result

    for result in vector_results:
        result['vector_score'] = result.pop('score', 0)
        title = result.get('title')
        if title in movie_results:
            movie_results[title].update(result)
        else:
            movie_results[title] = result        

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
            0.5 * atlas_norm +
            0.5 * vector_norm
        )


    results = sorted(
        movie_results.values(),
        key=lambda x: x.get("final_score",0),
        reverse=True
    )

    for movie in results[:10]:
        print(
            movie["title"],
            movie.get("atlas_score", 0),
            movie.get("vector_score", 0),
            atlas_norm,
            vector_norm,
            movie["final_score"]
        )
    print("MAX ATLAS:", max_atlas)
    print("MAX VECTOR:", max_vector)

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
