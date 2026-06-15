import model_and_database
from embedding import get_embedding

def vector_movie_recommendation(query: str):
    query_embedding = get_embedding(query)

    results = model_and_database.collection.aggregate(
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


    seen = set()
    for result in results:
        if result.get('title') in seen:
            continue
        seen.add(result.get('title'))
        combined_text = f"""
            Title: {result.get('title','')}
            Genres: {' '.join(result.get('genres', []))}  
            Year: {result.get('year','')}
            Directors: {' '.join(result.get('directors', []))}
            Plot: {result.get('plot','')}
            """
        print(combined_text)
