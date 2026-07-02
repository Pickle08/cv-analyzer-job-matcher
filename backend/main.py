from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import cv, jobs, analysis

app = FastAPI(title="AI Job Matcher API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# tambah ini — manual CORS headers di tiap response
@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

app.include_router(cv.router, prefix="/api/cv")
app.include_router(jobs.router, prefix="/api/jobs")
app.include_router(analysis.router, prefix="/api/analysis")

@app.get("/")
def health_check():
    return {"status": "ok"}
