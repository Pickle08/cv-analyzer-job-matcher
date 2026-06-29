import json
import asyncio
from playwright.async_api import async_playwright

async def scrape_page(page):
    jobs = []
    job_cards = await page.query_selector_all("div[class*='CompactJobCard']")

    seen_urls = set()

    for card in job_cards:
        try:
            title_el = await card.query_selector("h2[class*='JobTitle'] a")
            title = await title_el.inner_text() if title_el else "N/A"

            aria = await card.get_attribute("aria-label") or ""
            if "Company:" not in aria:
                parent = await card.query_selector("[aria-label*='Company']")
                aria = await parent.get_attribute("aria-label") if parent else ""

            company = "N/A"
            location = "N/A"
            if "Company:" in aria:
                company = aria.split("Company:")[1].split(",")[0].strip()
            if "Location:" in aria:
                location = aria.split("Location:")[1].strip()

            salary_el = await card.query_selector("span[class*='Salary']")
            salary = await salary_el.inner_text() if salary_el else "Tidak Ditampilkan"

            skills_raw = await card.get_attribute("data-gtm-job-card-info") or ""
            skills = [s.strip() for s in skills_raw.split(",") if s.strip() not in
                     ["experience", "salary", "logo", ""]]

            link_el = await card.query_selector("a[class*='JobCardTitle']")
            href = await link_el.get_attribute("href") if link_el else ""
            job_url = f"https://glints.com{href}" if href else "N/A"

            # skip duplikat
            if job_url in seen_urls:
                continue
            seen_urls.add(job_url)

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "salary": salary,
                "skills": skills,
                "url": job_url
            })

        except Exception as e:
            print(f"Error parsing card: {e}")
            continue

    return jobs

async def run_scraper():
    keywords = [
    # existing
    "data analyst",
    "data engineer",
    
    # tech
    "software engineer",
    "frontend developer",
    "backend developer",
    "fullstack developer",
    "mobile developer",
    "devops",
    "UI UX designer",
    "product manager",
    "data scientist",
    "business analyst",
    
    # general / publik
    "marketing",
    "digital marketing",
    "content creator",
    "social media specialist",
    "finance",
    "accounting",
    "tax",
    "audit",
    "human resources",
    "recruitment",
    "legal",
    "project manager",
    "supply chain",
    "logistic",
    "operations",
    "sales",
    "business development",
    "customer service",
    "procurement",
    "administration",
    "secretary",
    "public relations",
]  
    all_jobs = []
    seen_urls = set()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        for keyword in keywords:
            print(f"\nScraping keyword: '{keyword}'...")
            url = f"https://glints.com/id/opportunities/jobs/explore?keyword={keyword.replace(' ', '+')}&country=ID"
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await page.wait_for_timeout(2000)

            # scroll buat load lebih banyak jobs
            for i in range(5):
                await page.keyboard.press("End")
                await page.wait_for_timeout(1500)
                print(f"  Scroll {i+1}/5...")

            jobs = await scrape_page(page)

            # deduplikasi global
            for job in jobs:
                if job["url"] not in seen_urls:
                    seen_urls.add(job["url"])
                    all_jobs.append(job)

            print(f"  Dapat {len(jobs)} jobs dari '{keyword}'")

        print(f"\nTotal unik: {len(all_jobs)} jobs")

        with open("data/raw/glints_raw.json", "w", encoding="utf-8") as f:
            json.dump(all_jobs, f, indent=2, ensure_ascii=False)
        print("Saved to data/raw/glints_raw.json")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scraper())