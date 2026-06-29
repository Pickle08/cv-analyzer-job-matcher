# CV Analyzer & Job Matcher

An AI-powered web application that analyzes your CV and matches it with relevant job listings from Glints — complete with skill gap analysis and career recommendations.

---

## Features

-   **CV Analysis** — Upload your PDF CV and automatically extract skills and experience
-   **Semantic Job Matching** — Matches your CV to 1400+ job listings using Sentence Transformers (all-MiniLM-L6-v2)
-   **Skill Gap Analysis** — See exactly which skills you have vs. what the job requires
-   **Career Advice** — Get actionable recommendations on what to learn next
-   **Dark / Light Mode** — Toggle between themes
-   **Real Job Data** — Scraped from Glints Indonesia across 35+ job categories

---

## Tech Stack

### Frontend

-   React 19 + TypeScript + Vite
-   Tailwind CSS v3
-   React Router DOM

### Backend

-   FastAPI (Python)
-   PyMuPDF — PDF text extraction
-   Sentence Transformers — semantic similarity matching
-   SQLAlchemy + Supabase (PostgreSQL)

### Data Pipeline

-   Playwright — job scraping from Glints
-   Pandas — data cleaning & ETL
-   Supabase — cloud database storage

---

## Project Structure

```
cv-analyzer-job-matcher/
├── frontend/                  # React + TypeScript app
│   └── src/
│       ├── components/        # Navbar, JobCard, SkillBadge, UploadCV
│       ├── pages/             # Home, Result
│       ├── services/          # API calls
│       └── types/             # TypeScript interfaces
├── backend/                   # FastAPI server
│   └── app/
│       ├── routers/           # cv, jobs, analysis endpoints
│       ├── services/          # pdf_parser, matcher, gap, analysis
│       └── db/                # SQLAlchemy + Supabase connection
└── data-pipeline/             # Scraping & ETL
    ├── scraper/               # Playwright Glints scraper
    ├── etl/                   # clean, extract_skills, load_db
    └── data/                  # raw & cleaned job data
```

---

## How It Works

1. **User uploads a PDF CV** via the web interface
2. **Backend extracts text** from the PDF using PyMuPDF
3. **Skills are identified** by matching against a curated skills dictionary
4. **Semantic matching** compares CV content against 1400+ job listings using cosine similarity
5. **Top 3 matches** are returned with match score, skill gap, and career advice

---

## Getting Started

### Prerequisites

-   Python 3.10+
-   Node.js 18+
-   Supabase account

### 1. Clone the repository

```bash
git clone https://github.com/Pickle08/cv-analyzer-job-matcher.git
cd cv-analyzer-job-matcher
```

### 2. Setup backend

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` file in root:

```
DATABASE_URL=postgresql://postgres:[PASSWORD]@[HOST]:5432/postgres
```

Run backend:

```bash
uvicorn main:app --reload
```

### 3. Setup frontend

```bash
cd frontend
npm install
npm run dev
```

### 4. Run data pipeline (optional — database already seeded)

```bash
# Scrape jobs
python data-pipeline/scraper/glints_scraper.py

# ETL
python data-pipeline/etl/clean.py
python data-pipeline/etl/extract_skills.py
python data-pipeline/etl/load_db.py
```

---

## API Endpoints

| Method | Endpoint            | Description                   |
| ------ | ------------------- | ----------------------------- |
| POST   | `/api/cv/analyze`   | Upload PDF, extract skills    |
| POST   | `/api/jobs/match`   | Match CV to job listings      |
| POST   | `/api/analysis/gap` | Get skill gap + career advice |
| GET    | `/`                 | Health check                  |

Full API docs available at `http://localhost:8000/docs`

---

## Dataset

-   **1,425 job listings** scraped from Glints Indonesia
-   **35+ job categories** — from Data Engineering to Marketing, HR, Finance, and more
-   Updated: June 2026

---

## Author

**Ardhi Amin Darmawan**

-   GitHub: [@Pickle08](https://github.com/Pickle08)
-   LinkedIn: [linkedin.com/in/ardhi-amin](https://linkedin.com/in/ardhi-amin)

---

## License

MIT License — feel free to use and modify for your own portfolio.
