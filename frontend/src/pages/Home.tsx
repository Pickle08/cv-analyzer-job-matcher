import { UploadCV } from "../components/UploadCV";
import { Navbar } from "../components/Navbar";

interface HomeProps {
    isDark: boolean;
    toggleTheme: () => void;
}

export const Home = ({ isDark, toggleTheme }: HomeProps) => {
    return (
        <div className="min-h-screen bg-white dark:bg-gray-950">
            <Navbar isDark={isDark} toggleTheme={toggleTheme} />
            <main className="max-w-2xl mx-auto px-6 pt-24 pb-16">
                <p className="text-xs text-gray-400 dark:text-gray-500 uppercase tracking-widest mb-5">
                    AI-powered · Gratis
                </p>
                <h1 className="text-3xl font-medium text-gray-900 dark:text-white leading-snug tracking-tight mb-4">
                    CV kamu cocok untuk <br /> posisi apa?
                </h1>
                <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed mb-10 max-w-md">
                    Upload CV-mu dan temukan lowongan yang paling relevan dari
                    Glints — lengkap dengan skill gap analysis dan rekomendasi
                    karir.
                </p>
                <UploadCV />
                <div className="flex gap-8 mt-10 pt-8 border-t border-gray-100 dark:border-gray-800">
                    <div className="text-sm text-gray-400">
                        <span className="text-gray-900 dark:text-white font-medium">
                            68+
                        </span>{" "}
                        lowongan aktif
                    </div>
                    <div className="text-sm text-gray-400">
                        <span className="text-gray-900 dark:text-white font-medium">
                            Semantic
                        </span>{" "}
                        AI matching
                    </div>
                    <div className="text-sm text-gray-400">
                        <span className="text-gray-900 dark:text-white font-medium">
                            Real-time
                        </span>{" "}
                        gap analysis
                    </div>
                </div>
            </main>
        </div>
    );
};
