import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const searchMovies = async (query, mode) => {
    const response = await axios.get(
        `${API_URL}/recommend/${mode}`,
        {
            params: { query }
        }
    );

    return response.data;
};
export const compareModes =
    async (query) => {

    const [
        hybrid,
        vector,
        atlas
    ] = await Promise.all([

        searchMovies(query, "hybrid"),

        searchMovies(query, "vector"),

        searchMovies(query, "atlas")

    ]);

    return {
        hybrid,
        vector,
        atlas
    };
};