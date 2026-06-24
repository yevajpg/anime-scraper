import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://myanimelist.net/topanime.php"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
anime_list = soup.find_all("tr", class_="ranking-list")

data = []

for i, anime in enumerate(anime_list, start=1):
    title = anime.find("h3", class_="anime_ranking_h3")
    score = anime.find("span", class_="score-label")

    if title and score:
        data.append([i, title.text.strip(), score.text.strip()])

# Save as a proper Excel file
df = pd.DataFrame(data, columns=["Rank", "Title", "Score"])
df.to_excel("anime_top50.xlsx", index=False)

print("Done! Check anime_top50.xlsx")
