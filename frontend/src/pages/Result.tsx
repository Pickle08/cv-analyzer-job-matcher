import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { api } from "../services/api";
import type { JobMatch } from "../types/index.ts";
import { JobCard } from "../components/JobCard";
import { Navbar } from "../components/Navbar";
import { SkillBadge } from "../components/SkillBadge";

interface ResultProps {
    isDark: boolean;
    toggleTheme: () => void;
}

export const Result = ({ isDark, toggleTheme }: ResultProps) => {
    const { state } = useLocation();
    const navigate = useNavigate();
    const [jobs, setJobs] = useState<JobMatch[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const cvData = state?.cvData;
    const bestMatch = jobs[0];

    useEffect(() => {
        if (!cvData) {
            navigate("/");
            return;
        }

        const fetchMatches = async () => {
            try {
                const data = await api.matchJobs({
                    cv_text: cvData.full_text,
                    cv_skills: cvData.cv_skills,
                });
                setJobs(data.matches);
            } catch (err) {
                console.error("Gagal fetching matches", err);
                setError("Gagal mencari job matches. Coba upload ulang.");
            } finally {
                setLoading(false);
            }
        };

        fetchMatches();
    }, [state, navigate]);

    if (error)
        return (
            <div className="min-h-screen bg-white dark:bg-gray-950 flex items-center justify-center">
                <div className="text-center">
                    <p className="text-sm text-red-500 mb-4">{error}</p>
                    <button
                        onClick={() => navigate("/")}
                        className="text-sm text-gray-600 dark:text-gray-400 underline">
                        Kembali
                    </button>
                </div>
            </div>
        );

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-950">
            <Navbar isDark={isDark} toggleTheme={toggleTheme} />

            {loading ? (
                <div className="flex items-center justify-center h-64">
                    <p className="text-sm text-gray-400">
                        Sedang mencari pekerjaan yang cocok...
                    </p>
                </div>
            ) : (
                <div className="max-w-6xl mx-auto px-6 py-10 flex gap-6 items-start">
                    {/* SIDEBAR */}
                    <aside className="w-64 shrink-0 flex flex-col gap-4">
                        {/* CV info */}
                        <div className="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-xl p-4">
                            <p className="text-xs text-gray-400 uppercase tracking-widest mb-3">
                                CV Dianalisis
                            </p>
                            <p className="text-sm font-medium text-gray-900 dark:text-white">
                                {cvData?.filename?.replace(".pdf", "")}
                            </p>
                            <p className="text-xs text-gray-400 mt-1">
                                Informatics Engineering
                            </p>
                        </div>

                        {/* Skills ditemukan */}
                        <div className="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-xl p-4">
                            <p className="text-xs text-gray-400 uppercase tracking-widest mb-3">
                                Skills Ditemukan
                            </p>
                            <div className="flex flex-wrap gap-1.5">
                                {cvData?.cv_skills?.length > 0 ? (
                                    cvData.cv_skills.map((skill: string) => (
                                        <SkillBadge
                                            key={skill}
                                            skill={skill}
                                            variant="matched"
                                        />
                                    ))
                                ) : (
                                    <p className="text-xs text-gray-400">
                                        Tidak ada skill terdeteksi
                                    </p>
                                )}
                            </div>
                        </div>

                        {/* Perlu dipelajari */}
                        {bestMatch &&
                            bestMatch.gap_analysis.missing.length > 0 && (
                                <div className="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-xl p-4">
                                    <p className="text-xs text-gray-400 uppercase tracking-widest mb-3">
                                        Perlu Dipelajari
                                    </p>
                                    <div className="flex flex-wrap gap-1.5">
                                        {bestMatch.gap_analysis.missing.map(
                                            (skill) => (
                                                <SkillBadge
                                                    key={skill}
                                                    skill={skill}
                                                    variant="missing"
                                                />
                                            )
                                        )}
                                    </div>
                                </div>
                            )}

                        {/* Best match score */}
                        {bestMatch && (
                            <div className="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-xl p-4 text-center">
                                <p className="text-4xl font-medium text-gray-900 dark:text-white tracking-tight">
                                    {bestMatch.match_score}%
                                </p>
                                <p className="text-xs text-gray-400 mt-1">
                                    match terbaik
                                </p>
                            </div>
                        )}
                    </aside>

                    {/* MAIN CONTENT */}
                    <main className="flex-1 flex flex-col gap-4">
                        <div className="flex items-center justify-between">
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                                {jobs.length} lowongan ditemukan
                            </p>
                            <button
                                onClick={() => navigate("/")}
                                className="text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 transition-colors">
                                ← Upload ulang
                            </button>
                        </div>
                        {jobs.map((job, idx) => (
                            <JobCard key={idx} job={job} />
                        ))}
                    </main>
                </div>
            )}
        </div>
    );
};
