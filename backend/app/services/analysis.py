from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gap import get_skill_gap

router = APIRouter()

class AnalysisRequest(BaseModel):
    cv_skills: list[str]
    job_skills: list[str]

def generate_career_advice(cv_skills: list, missing_skills: list) -> str:
    if not missing_skills:
        return "CV kamu sudah sangat relevan dengan lowongan ini! Terus tingkatkan pengalaman proyekmu."
    
    top_missing = missing_skills[:3]
    advice = f"Untuk meningkatkan peluangmu di posisi ini, fokuslah mempelajari: {', '.join(top_missing)}. "
    
    if len(missing_skills) > 5:
        advice += "Kesenjangan skill cukup besar, pertimbangkan untuk mengambil sertifikasi atau bootcamp."
    else:
        advice += "Kamu sudah cukup dekat, coba buat 1 proyek kecil yang mencakup skill tersebut."
        
    return advice

@router.post("/gap")
async def analyze_gap(data: AnalysisRequest):
    gap = get_skill_gap(data.cv_skills, data.job_skills)
    advice = generate_career_advice(data.cv_skills, gap["missing"])
    
    return {
        "matched": gap["matched"],
        "missing": gap["missing"],
        "match_percentage": gap["match_percentage"],
        "advice": advice
    }