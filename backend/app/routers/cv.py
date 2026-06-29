import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_parser import extract_text_from_pdf, extract_skills_from_text
import os

router = APIRouter()

@router.post("/analyze")
async def analyze_cv(file: UploadFile = File(...)):
    # Gunakan nama file unik agar tidak bentrok
    temp_file_path = f"temp_{file.filename}"
    
    try:
        # Simpan file ke disk dulu
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Proses dari path
        text = extract_text_from_pdf(temp_file_path)
        skills = extract_skills_from_text(text)
        
        return {
            "filename": file.filename,
            "cv_skills": skills,
            "full_text": text[:500]
        }
    except Exception as e:
        # Print error detail ke terminal agar kita tahu isinya
        print(f"ERROR DETAILS: {str(e)}") 
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Selalu hapus file sampah
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)