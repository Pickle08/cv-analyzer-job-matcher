import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables dari .env di root
load_dotenv()

def load_to_db():
    # Path ke file hasil ekstraksi skill
    file_path = "data/cleaned/jobs_with_skills.csv"
    
    if not os.path.exists(file_path):
        print("File jobs_with_skills.csv tidak ditemukan. Jalankan extract_skills.py dulu.")
        return

    # Ambil connection string dari environment variable
    # Pastikan di root folder kamu ada file .env berisi: DATABASE_URL=postgresql://...
    db_url = os.getenv("DATABASE_URL")
    
    if not db_url:
        print("Error: DATABASE_URL tidak ditemukan di .env")
        return

    df = pd.read_csv(file_path)
    engine = create_engine(db_url)
    
    # Masukkan ke tabel 'jobs'
    # if_exists='replace' akan membuat ulang tabel setiap kali script dijalankan
    df.to_sql('jobs', engine, if_exists='replace', index=False)
    print(f"Berhasil! {len(df)} lowongan telah dimuat ke database.")

if __name__ == "__main__":
    load_to_db()