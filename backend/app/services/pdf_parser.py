import fitz
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def extract_text_from_pdf(file_path: str) -> str:
    try:
        with fitz.open(file_path) as doc:
            text = "".join([page.get_text() for page in doc])
        if not text.strip():
            raise ValueError("PDF kosong atau tidak bisa dibaca")
        return text.strip()
    except Exception as e:
        raise RuntimeError(f"Gagal membaca PDF: {str(e)}")

def extract_skills_from_text(text: str) -> list:
    skills_path = os.path.join(BASE_DIR, "data", "skills_list.json")
    
    if not os.path.exists(skills_path):
        raise FileNotFoundError(f"File JSON tidak ditemukan di: {skills_path}")
        
    with open(skills_path, "r") as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        all_skills = [skill for category in data.values() for skill in category]
    else:
        all_skills = data
    
    text_lower = text.lower()
    return [skill for skill in all_skills if skill.lower() in text_lower]

if __name__ == "__main__":
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"skills_path: {os.path.join(BASE_DIR, 'data', 'skills_list.json')}")
    print(f"File exists: {os.path.exists(os.path.join(BASE_DIR, 'data', 'skills_list.json'))}")