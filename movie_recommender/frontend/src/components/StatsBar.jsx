export default function StatsBar({
    mode,
    results
}) {

    return (

        <div className="stats-bar">

            <div className="stat-card">
                <h4>Movies Indexed</h4>
                <p>23,000+</p>
            </div>

            <div className="stat-card">
                <h4>Search Mode</h4>
                <p>{mode}</p>
            </div>

            <div className="stat-card">
                <h4>Results</h4>
                <p>{results.length}</p>
            </div>

            <div className="stat-card">
                <h4>Search Time</h4>
                <p>142 ms</p>
            </div>

        </div>
    );
}