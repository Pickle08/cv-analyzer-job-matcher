export interface CVAnalysisResult {
    filename: string;
    cv_skills: string[];
    full_text: string;
}

export interface GapAnalysis {
    matched: string[];
    missing: string[];
    match_percentage: number;
}

export interface JobMatch {
    title: string;
    company: string;
    location: string;
    salary: string;
    skills: string;
    url: string;
    match_score: number;
    gap_analysis: GapAnalysis;
    coaching_advice: string;
}

export interface JobMatchResult {
    matches: JobMatch[];
}
