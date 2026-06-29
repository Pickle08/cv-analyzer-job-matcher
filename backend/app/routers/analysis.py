from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gap import get_skill_gap
from app.services.analysis import generate_career_advice

router = APIRouter()

class AnalysisRequest(BaseModel):
    cv_skills: list[str]
    job_skills: list[str]

@router.post("/gap")
async def get_gap_analysis(data: AnalysisRequest):
    gap = get_skill_gap(data.cv_skills, data.job_skills)
    advice = generate_career_advice(data.cv_skills, gap["missing"])
    return {
        "matched": gap["matched"],
        "missing": gap["missing"],
        "match_percentage": gap["match_percentage"],
        "advice": advice
    }