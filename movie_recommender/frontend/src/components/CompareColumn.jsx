export default function CompareColumn({
    title,
    movies
}) {

    return (

        <div>

            <h3>{title}</h3>

            {movies
                .slice(0, 5)
                .map(movie => (

                    <div
                        className="compare-item"
                        key={movie.title}
                    >

                        <img
                            src={movie.poster}
                            alt={movie.title}
                        />

                        <div>

                            <h4>
                                {movie.title}
                            </h4>

                            <p>
                                score:
                                {" "}
                                {movie.score}
                            </p>

                        </div>

                    </div>

                ))
            }

        </div>

    );
}