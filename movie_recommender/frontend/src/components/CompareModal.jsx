export default function CompareModal({
    results,
    onClose
}) {

    return (

        <div className="compare-overlay">

            <div className="compare-modal">

                <button
                    className="close-btn"
                    onClick={onClose}
                >
                    ✕
                </button>

                <h2>
                    Compare Search Modes
                </h2>

                <div className="compare-grid">

                    {[
                        {
                            title: "Hybrid",
                            movies: results.hybrid
                        },
                        {
                            title: "Vector",
                            movies: results.vector
                        },
                        {
                            title: "Atlas",
                            movies: results.atlas
                        }
                    ].map((section) => (

                        <div
                            key={section.title}
                            className="compare-column"
                        >

                            <h3>
                                {section.title}
                            </h3>

                            {section.movies
                                .slice(0, 5)
                                .map((movie, index) => (

                                    <div
                                        key={index}
                                        className="compare-card"
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
                                                ⭐ {movie.score}
                                            </p>

                                        </div>

                                    </div>

                                ))
                            }

                        </div>

                    ))}

                </div>

            </div>

        </div>

    );
}