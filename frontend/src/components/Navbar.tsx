interface NavbarProps {
    isDark: boolean;
    toggleTheme: () => void;
}

export const Navbar = ({ isDark, toggleTheme }: NavbarProps) => {
    return (
        <nav className="border-b border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-950 px-6 py-3 flex items-center justify-between sticky top-0 z-10">
            <div className="flex items-center gap-2">
                <span className="text-sm font-medium text-gray-900 dark:text-white tracking-tight">
                    cvmatcher
                </span>
            </div>
            <div className="flex items-center gap-1">
                <a
                    href="#"
                    className="text-sm text-gray-500 dark:text-gray-400 hover:text-gray-800 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800 px-3 py-1.5 rounded-md transition-colors">
                    Cara kerja
                </a>
                <a
                    href="https://github.com/Pickle08"
                    target="_blank"
                    rel="noreferrer"
                    className="text-sm text-gray-500 dark:text-gray-400 hover:text-gray-800 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800 px-3 py-1.5 rounded-md transition-colors">
                    GitHub
                </a>
                {/* toggle button */}
                <button
                    onClick={toggleTheme}
                    className="ml-2 p-1.5 rounded-md text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
                    {isDark ? "☀️" : "🌙"}
                </button>
                <a
                    href="/"
                    className="text-sm text-white bg-gray-900 dark:bg-white dark:text-gray-900 hover:bg-gray-700 px-3 py-1.5 rounded-md transition-colors ml-1">
                    Upload CV
                </a>
            </div>
        </nav>
    );
};
