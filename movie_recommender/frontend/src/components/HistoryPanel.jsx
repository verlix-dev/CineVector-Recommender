export default function HistoryPanel({
    history,
    setQuery
}) {

    return (

        <div className="history-panel">

            <h3>
                Recent Searches
            </h3>

            {history.length === 0 ? (

                <p>
                    Your searches will appear here.
                </p>

            ) : (

                history.map((item, index) => (

                    <div
                        key={index}
                        className="history-item"
                        onClick={() =>
                            setQuery(item)
                        }
                    >
                        {item}
                    </div>

                ))

            )}

        </div>

    );
}