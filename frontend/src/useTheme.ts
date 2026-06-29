import { useState, useEffect } from "react";

export const useTheme = () => {
    const [isDark, setIsDark] = useState(false);

    useEffect(() => {
        const root = document.documentElement;
        if (isDark) {
            root.classList.add("dark");
        } else {
            root.classList.remove("dark");
        }
    }, [isDark]);

    const toggleTheme = () => {
        console.log("toggle clicked, isDark:", isDark);
        setIsDark((prev) => !prev);
    };

    return { isDark, toggleTheme };
};
