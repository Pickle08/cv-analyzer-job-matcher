import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { Result } from "./pages/Result";
import { useTheme } from "./useTheme";

function App() {
    const { isDark, toggleTheme } = useTheme();

    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/"
                    element={<Home isDark={isDark} toggleTheme={toggleTheme} />}
                />
                <Route
                    path="/result"
                    element={
                        <Result isDark={isDark} toggleTheme={toggleTheme} />
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
