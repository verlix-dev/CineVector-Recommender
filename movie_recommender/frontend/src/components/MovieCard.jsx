export default function MovieCard({
    movie
}) {

    return (

        <div className="movie-card">
            <img
    src={movie.poster}
    alt={movie.title}
    className="movie-poster"
/>
            <h2>
                {movie.title}
            </h2>

            <div>
                ⭐ {movie.score}
            </div>

            <p>
                {movie.year}
            </p>

            <p>
                {
                    movie.genres?.join(
                        ", "
                    )
                }
            </p>

            <p>
                {movie.plot}
            </p>

        </div>
    );
}