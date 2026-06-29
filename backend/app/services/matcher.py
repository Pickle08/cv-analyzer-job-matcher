from sentence_transformers import SentenceTransformer, util
import pandas as pd
from app.db.database import engine

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_best_matches(cv_text: str, top_k: int = 5):
    # 1. ambil jobs dari Supabase
    query = "SELECT title, company, location, salary, skills_normalized, url FROM jobs"
    df_jobs = pd.read_sql(query, engine)
    
    # 2. isi NaN dengan string kosong
    df_jobs['skills_normalized'] = df_jobs['skills_normalized'].fillna('')
    
    # 3. encode CV dan jobs
    cv_embedding = model.encode(cv_text, convert_to_tensor=True)
    job_embeddings = model.encode(df_jobs['skills_normalized'].tolist(), convert_to_tensor=True)
    
    # 4. cosine similarity
    cosine_scores = util.cos_sim(cv_embedding, job_embeddings)[0]
    
    # 5. top K results
    top_indices = cosine_scores.argsort(descending=True)[:top_k]
    
    matches = []
    for idx in top_indices:
        matches.append({
            "title": df_jobs.iloc[idx.item()]['title'],
            "company": df_jobs.iloc[idx.item()]['company'],
            "location": df_jobs.iloc[idx.item()]['location'],
            "salary": df_jobs.iloc[idx.item()]['salary'],
            "skills": df_jobs.iloc[idx.item()]['skills_normalized'],
            "url": df_jobs.iloc[idx.item()]['url'],
            "match_score": round(cosine_scores[idx].item() * 100, 2)
        })
    
    return matches