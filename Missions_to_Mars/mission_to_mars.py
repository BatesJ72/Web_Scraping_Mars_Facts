import requests
from bs4 import BeautifulSoup

URL = "https://mars.nasa.gov/news/"

BASE_PARAMS = {
    "page": 0,
    "per_page": 40,
    "order": "publish_date+desc%2Ccreated_at+desc",
    # "search": ,
    "category": "19%2C165%2C184%2C204",
    "blank_scope": "Latest",
}

# r = requests.get(URL)
r = requests.get(URL, params = BASE_PARAMS)

# print(r.status_code)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
# print(soup.find(class_="content_title").text.strip())
title = soup.find(class_="content_title").text.strip()
print(title)
# print(soup.find(class_="content_title").find_all("p").text.strip())
# print(soup.find(class_="article_teaser_body"))
text = soup.find("p").text
print(text)

