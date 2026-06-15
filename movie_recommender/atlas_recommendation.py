import model_and_database
from embedding import get_embedding



def atlas_movie_recommendation(query: str):

    results = model_and_database.collection.aggregate([
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

    seen = set()

    for result in results:
        title = result.get("title")

        if title in seen:
            continue

        seen.add(title)

        print(f"""
                    Title: {title}
                    Genres: {' '.join(result.get('genres', []))}
                    Year: {result.get('year', '')}
                    Directors: {' '.join(result.get('directors', []))}
                    Score: {result.get('score', 0):.4f}
                    Plot: {result.get('plot', '')}
                """)
    # seen = set()
    # for result in results:
    #     if result.get('title') in seen:
    #         continue
    #     seen.add(result.get('title'))
    #     combined_text = f"""
    #         Title: {result.get('title','')}
    #         Genres: {' '.join(result.get('genres', []))}  
    #         Year: {result.get('year','')}
    #         Directors: {' '.join(result.get('directors', []))}
    #         Plot: {result.get('plot','')}
    #         """
    #     print(combined_text)