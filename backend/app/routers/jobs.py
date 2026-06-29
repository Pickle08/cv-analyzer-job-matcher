from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.matcher import get_best_matches
from app.services.gap import get_skill_gap
from app.routers.analysis import generate_career_advice

router = APIRouter()

class MatchRequest(BaseModel):
    cv_text: str
    cv_skills: list[str]

@router.post("/match")
async def match_jobs(data: MatchRequest):
    matches = get_best_matches(data.cv_text, top_k=3)
    
    for job in matches:
        job_skills = job.get('skills', '').split(', ')
        gap = get_skill_gap(data.cv_skills, job_skills)
        job['gap_analysis'] = gap
        job['coaching_advice'] = generate_career_advice(data.cv_skills, gap['missing'])
        
    return {"matches": matches}