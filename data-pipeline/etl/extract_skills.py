import pandas as pd
import json

def extract_skills():
    df = pd.read_csv("data/cleaned/cleaned_jobs.csv")
    
    with open("data/skills_list.json", "r") as f:
        skills_master = json.load(f)
    
    all_skills = [skill for category in skills_master.values() for skill in category]
    
    # mapping skills berdasarkan job title
    title_skill_map = {
    "data analyst": ["SQL", "Python", "Data Analysis", "Microsoft Excel",
                    "Power BI", "Statistics", "Data Visualization"],
    "data engineer": ["Python", "SQL", "Spark", "Airflow", "PostgreSQL",
                     "BigQuery", "Kafka", "dbt", "Hadoop"],
    }
    
    def find_skills(row):
        found = set()
        
        # 1. cek dari kolom skills yang ada (kalau ga kosong)
        skills_raw = str(row.get('skills', ''))
        if skills_raw and skills_raw != 'nan':
            for s in all_skills:
                if s.lower() in skills_raw.lower():
                    found.add(s)
        
        # 2. fallback: infer dari job title
        title = str(row.get('title', '')).lower()
        for key, skills in title_skill_map.items():
            if key in title:
                found.update(skills)
                break
        
        return ", ".join(sorted(found))
    
    df['skills_normalized'] = df.apply(find_skills, axis=1)
    
    df.to_csv("data/cleaned/jobs_with_skills.csv", index=False)
    print(f"Selesai! {len(df)} jobs tersimpan.")
    print("\nSample:")
    print(df[['title', 'company', 'skills_normalized']].head(5).to_string())

if __name__ == "__main__":
    extract_skills()