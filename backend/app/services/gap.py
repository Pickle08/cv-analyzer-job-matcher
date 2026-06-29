def get_skill_gap(cv_skills: list, job_skills: list):
    cv_skills_set = set(s.lower().strip() for s in cv_skills if s)
    job_skills_set = set(s.lower().strip() for s in job_skills if s)
    
    matched_lower = cv_skills_set.intersection(job_skills_set)
    missing_lower = job_skills_set - cv_skills_set

    # kembalikan dengan kapitalisasi asli dari job_skills
    job_skills_map = {s.lower().strip(): s for s in job_skills if s}
    
    matched = [job_skills_map.get(s, s) for s in matched_lower]
    missing = [job_skills_map.get(s, s) for s in missing_lower]

    return {
        "matched": sorted(matched),
        "missing": sorted(missing),
        "match_percentage": round((len(matched) / len(job_skills_set) * 100), 2) if job_skills_set else 100
    }