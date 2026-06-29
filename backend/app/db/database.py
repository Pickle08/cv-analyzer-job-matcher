import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("DEBUG: DATABASE_URL KOSONG! Cek Variable di Dashboard Railway.")
else:
    print(f"DEBUG: DATABASE_URL terbaca: {DATABASE_URL[:15]}******")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,      # cek koneksi sebelum dipakai
    pool_recycle=300,        # recycle koneksi tiap 5 menit
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()