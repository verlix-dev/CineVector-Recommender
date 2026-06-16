import { useState } from "react";

import Navbar from "../components/Navbar";
import SearchBar from "../components/SearchBar";
import ModeSelector from "../components/ModeSelector";
import MovieGrid from "../components/MovieGrid";
import StatsBar from "../components/StatsBar";
import { searchMovies } from "../services/api";
import CompareModal from "../components/CompareModal";
import HistoryPanel from "../components/HistoryPanel";


export default function Home() {
    const [compareResults, setCompareResults] =
    useState(null);
    const [showCompare, setShowCompare] =
    useState(false);
    const [query, setQuery] =
    useState("");
    const [movies, setMovies] = useState([]);
    const [history, setHistory] = useState([]);
    const [mode, setMode] = useState("hybrid");
    const handleCompare = async () => {
        console.log("Compare clicked");
            if (!query) return;

            const [
                hybrid,
                vector,
                atlas
            ] = await Promise.all([

                searchMovies(query, "hybrid"),

                searchMovies(query, "vector"),

                searchMovies(query, "atlas")

            ]);

            console.log({
                hybrid,
                vector,
                atlas
            });

            setCompareResults({
                hybrid,
                vector,
                atlas
            }); setShowCompare(true);
};
console.log(compareResults);
console.log(showCompare);
    return (
        <div>

            <Navbar />


<SearchBar
    query={query}
    setQuery={setQuery}
    mode={mode}
    setMovies={setMovies}
    setHistory={setHistory}
/>

<ModeSelector
    mode={mode}
    setMode={setMode}
    onCompare={handleCompare}
/>
            <StatsBar
                mode={mode}
                results={movies}
            />
            <HistoryPanel
    history={history}
    setQuery={setQuery}
/>

            <MovieGrid
                movies={movies}
                mode={mode}
            />
{
    showCompare && (
        <CompareModal
            results={compareResults}
            onClose={() =>
                setShowCompare(false)
            }
        />
    )
}
    


        </div>
    );
}