import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://habr.com/ru/articles/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text
soup = BeautifulSoup(html, "html.parser")

def parse():
    articles = []
    for item in soup.select("article.tm-articles-list__item"):   # блок статьи
        link_tag = item.select_one("h2.tm-title a")             # заголовок и ссылка
        time_tag = item.find("time")

        if link_tag:
            title = link_tag.text.strip()
            link = link_tag["href"]
            if link.startswith("/"):
                link = "https://habr.com" + link  # дополняем относительный путь

            published = time_tag["datetime"] if time_tag and "datetime" in time_tag.attrs else datetime.utcnow().isoformat()

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




