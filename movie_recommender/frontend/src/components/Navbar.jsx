import { Sparkles } from "lucide-react";

export default function Navbar() {
    return (
        <header className="navbar">

            <div className="logo">

                <Sparkles size={20} />

                <span>
                    MovieMind AI
                </span>

            </div>

        </header>
    );
}