# Anime top 50 scraper

A Python web scraper that pulls the top 50 anime from MyAnimeList and saves them to an Excel file with rankings and scores.

## What it does
- Scrapes real-time data from MyAnimeList
- Extracts title, rank, and score for each anime
- Saves everything to a clean Excel file

## Libraries used
- `requests` — fetching web pages
- `BeautifulSoup` — parsing HTML
- `pandas` — saving to Excel

## How to run
1. Install dependencies: `pip install requests beautifulsoup4 pandas openpyxl`
2. Run: `python app.py`
3. Open `anime_top50.xlsx`