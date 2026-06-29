import type { CVAnalysisResult, JobMatchResult } from "../types/index.ts";

const BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api";

export const api = {
    analyzeCV: async (file: File): Promise<CVAnalysisResult> => {
        const formData = new FormData();
        formData.append("file", file);
        const response = await fetch(`${BASE_URL}/cv/analyze`, {
            method: "POST",
            body: formData,
        });
        if (!response.ok) throw new Error("Gagal menganalisis CV");
        return response.json();
    },

    matchJobs: async (cvData: {
        cv_text: string;
        cv_skills: string[];
    }): Promise<JobMatchResult> => {
        const response = await fetch(`${BASE_URL}/jobs/match`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(cvData),
        });
        if (!response.ok) throw new Error("Gagal mencari job matches");
        return response.json();
    },
};
