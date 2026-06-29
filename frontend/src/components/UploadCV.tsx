import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../services/api";

export const UploadCV = () => {
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [dragOver, setDragOver] = useState(false);

    const handleUpload = async (file: File) => {
        if (!file.name.endsWith(".pdf")) {
            alert("Hanya file PDF yang diterima");
            return;
        }
        setLoading(true);
        try {
            const result = await api.analyzeCV(file);
            navigate("/result", { state: { cvData: result } });
        } catch (err) {
            console.error("Gagal:", err);
            alert("Gagal menganalisis CV. Coba lagi.");
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files?.[0]) handleUpload(e.target.files[0]);
    };

    const handleDrop = (e: React.DragEvent) => {
        e.preventDefault();
        setDragOver(false);
        if (e.dataTransfer.files?.[0]) handleUpload(e.dataTransfer.files[0]);
    };

    return (
        <label
            className={`block border border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors
        ${
            dragOver
                ? "border-gray-400 bg-gray-50 dark:bg-gray-800"
                : "border-gray-300 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500"
        } dark:bg-gray-900`}
            onDragOver={(e) => {
                e.preventDefault();
                setDragOver(true);
            }}
            onDragLeave={() => setDragOver(false)}
            onDrop={handleDrop}>
            <input
                type="file"
                accept=".pdf"
                onChange={handleInputChange}
                disabled={loading}
                className="hidden"
            />
            <div className="text-3xl mb-3">📄</div>
            {loading ? (
                <div>
                    <p className="text-sm font-medium text-gray-700">
                        Menganalisis CV...
                    </p>
                    <p className="text-xs text-gray-400 mt-1">
                        Mohon tunggu sebentar
                    </p>
                </div>
            ) : (
                <div>
                    <p className="text-sm font-medium text-gray-700 dark:text-gray-200">
                        Upload CV kamu
                    </p>
                    <p className="text-xs text-gray-400 mt-1">
                        PDF · maksimal 5MB
                    </p>
                    <div className="mt-4 inline-block bg-gray-900 dark:bg-white dark:text-gray-900 text-white text-sm px-4 py-2 rounded-md">
                        Pilih file
                    </div>
                </div>
            )}
        </label>
    );
};
