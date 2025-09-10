import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://en.wikipedia.org/wiki/Portal:Current_events"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text
soup = BeautifulSoup(html, "html.parser")

def parse():
    articles = []
    # проходим по дням (заголовки h3 = даты)
    for day_block in soup.select("div.vevent"):
        date_tag = day_block.find("h3")  # дата блока
        published = date_tag.text.strip() if date_tag else datetime.utcnow().isoformat()

        # вытаскиваем статьи в этом блоке
        for li in day_block.select("ul > li"):
            link_tag = li.find("a")
            if link_tag and "href" in link_tag.attrs:
                title = link_tag.text.strip()
                link = "https://en.wikipedia.org" + link_tag["href"]

                articles.append({
                    "title": title,
                    "link": link,
                    "published": published
                })
    return articles

if __name__ == "__main__":
    data = parse()
    data = parse()  # здесь получаем список статей
    with open("/opt/airflow/data/out.json", "w", encoding="utf-8") as f:
        import json
        json.dump(data, f, ensure_ascii=False, indent=2)    




