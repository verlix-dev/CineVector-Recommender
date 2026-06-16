import MovieCard from "./MovieCard";

export default function MovieGrid({
    movies
}) {

    return (

        <div className="movie-grid">

            {movies.map(
                (movie, i) => (

                    <MovieCard
                        key={i}
                        movie={movie}
                    />

                )
            )}

        </div>
    );
}