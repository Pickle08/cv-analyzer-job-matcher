from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cv, jobs, analysis

app = FastAPI(title="AI Job Matcher API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cv.router, prefix="/api/cv")
app.include_router(jobs.router, prefix="/api/jobs")
app.include_router(analysis.router, prefix="/api/analysis")

@app.get("/")
def health_check():
    return {"status": "ok"}
