import { Search, Sparkle, WandSparkles,Sparkles } from "lucide-react";
import { searchMovies } from "../services/api";

export default function SearchBar({
    query,
    setQuery,
    mode,
    setMovies,
    setHistory
})
{

    const handleSearch = async () => {

        if (!query) return;

        const results =
            await searchMovies(
                query,
                mode
            );

        setMovies(results);
        setHistory(prev => [
            query,
            ...prev.filter(item => item !== query)
        ].slice(0, 5));
    }; 

    return (
        <div className="hero">

            <h1>MovieMind AI</h1>

            <div className="search-box">

                <input
                    value={query}
                    onChange={(e) =>
                        setQuery(e.target.value)
                    }
                    placeholder="Describe a movie..."
                />

                <button
    className="search-btn"
    onClick={handleSearch}
>
    <WandSparkles size={18} />
    Search
</button>

            </div>

        </div>
        
    );
    
    
}   