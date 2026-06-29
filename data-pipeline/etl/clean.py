import json
import re
import pandas as pd
import os

def clean_html(text):
    if not isinstance(text, str):
        return ""
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_data():
    input_path = "data/raw/glints_raw.json"       # fix nama file
    output_path = "data/cleaned/cleaned_jobs.csv"

    if not os.path.exists(input_path):
        print(f"File {input_path} tidak ditemukan. Jalankan scraper dulu.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    print(f"Data awal: {len(df)} rows")

    # 1. Buang duplikat
    df = df.drop_duplicates(subset=['title', 'company', 'url'])

    # 2. Bersihkan description kalau ada
    if 'description' in df.columns:
        df['description'] = df['description'].apply(clean_html)

    # 3. Filter judul kosong atau N/A
    df = df[df['title'].str.strip() != '']
    df = df[df['title'] != 'N/A']
    df = df[df['company'] != 'N/A']

    # 4. Konversi skills list jadi string
    df['skills'] = df['skills'].apply(
        lambda x: ', '.join(x) if isinstance(x, list) else x
    )

    # 5. Reset index
    df = df.reset_index(drop=True)

    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data bersih: {len(df)} lowongan tersimpan di {output_path}")

if __name__ == "__main__":
    clean_data()