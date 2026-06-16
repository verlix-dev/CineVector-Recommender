export default function ModeSelector({
    mode,
    setMode,
    onCompare
}) {

    return (

        <div className="mode-selector">

            {[
                "hybrid",
                "vector",
                "atlas"
            ].map((m) => (

                <button
                    key={m}
                    className={
                        mode === m
                            ? "active"
                            : ""
                    }
                    onClick={() =>
                        setMode(m)
                    }
                >
                    {m.charAt(0).toUpperCase() + m.slice(1)}
                </button>

            ))}

            <button
                className="compare-mode-btn"
                onClick={onCompare}
            >
                Compare Modes
            </button>

        </div>

    );
}