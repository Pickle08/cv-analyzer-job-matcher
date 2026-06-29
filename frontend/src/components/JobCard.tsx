import type { JobMatch } from "../types/index.ts";
import { SkillBadge } from "./SkillBadge";

export const JobCard = ({ job }: { job: JobMatch }) => {
    const scoreColor =
        job.match_score >= 70
            ? "text-green-600 dark:text-green-400"
            : job.match_score >= 40
            ? "text-amber-600 dark:text-amber-400"
            : "text-gray-500 dark:text-gray-400";

    return (
        <div className="bg-white dark:bg-gray-900 p-5 rounded-lg border border-gray-100 dark:border-gray-800 hover:border-gray-300 dark:hover:border-gray-700 transition-colors duration-200">
            {/* header */}
            <div className="flex justify-between items-start mb-3">
                <div>
                    <h2 className="text-sm font-semibold text-gray-900 dark:text-white">
                        {job.title}
                    </h2>
                    <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                        {job.company} · {job.location}
                    </p>
                    <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">
                        {job.salary}
                    </p>
                </div>
                <span className={`text-sm font-medium ${scoreColor}`}>
                    {job.match_score}%
                </span>
            </div>

            {/* matched skills */}
            {job.gap_analysis.matched.length > 0 && (
                <div className="mb-3">
                    <p className="text-xs text-gray-400 dark:text-gray-500 uppercase tracking-widest mb-1.5">
                        Matched
                    </p>
                    <div className="flex flex-wrap gap-1.5">
                        {job.gap_analysis.matched.map((skill) => (
                            <SkillBadge
                                key={skill}
                                skill={skill}
                                variant="matched"
                            />
                        ))}
                    </div>
                </div>
            )}

            {/* missing skills */}
            <div className="mb-3">
                <p className="text-xs text-gray-400 dark:text-gray-500 uppercase tracking-widest mb-1.5">
                    Missing
                </p>
                <div className="flex flex-wrap gap-1.5">
                    {job.gap_analysis.missing.length > 0 ? (
                        job.gap_analysis.missing.map((skill) => (
                            <SkillBadge
                                key={skill}
                                skill={skill}
                                variant="missing"
                            />
                        ))
                    ) : (
                        <span className="text-xs text-green-600 dark:text-green-400">
                            Perfect match!
                        </span>
                    )}
                </div>
            </div>

            {/* career insight */}
            <div className="pt-3 border-t border-gray-100 dark:border-gray-800">
                <p className="text-xs text-gray-400 dark:text-gray-500 leading-relaxed">
                    {job.coaching_advice}
                </p>
            </div>

            {/* link */}
            <a
                href={job.url}
                target="_blank"
                rel="noreferrer"
                className="mt-3 inline-flex items-center gap-1 text-xs text-gray-400 dark:text-gray-500 hover:text-gray-700 dark:hover:text-gray-200 transition-colors">
                Lihat di Glints →
            </a>
        </div>
    );
};
