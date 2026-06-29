interface SkillBadgeProps {
    skill: string;
    variant?: "matched" | "missing";
}

export const SkillBadge = ({ skill, variant = "missing" }: SkillBadgeProps) => {
    const styles = {
        matched:
            "bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 border-green-200 dark:border-green-800",
        missing:
            "bg-red-100 dark:bg-red-900 text-red-600 dark:text-red-300 border-red-100 dark:border-red-800",
    };

    return (
        <span
            className={`px-2 py-1 rounded-md text-xs font-semibold border ${styles[variant]}`}>
            {skill}
        </span>
    );
};
