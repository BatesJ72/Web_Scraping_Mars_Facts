import requests
from bs4 import BeautifulSoup
import pandas as pd 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# NASA Mars News

URL_NMN = "https://mars.nasa.gov/news/"

BASE_PARAMS_NMN = {
    "page": 0,
    "per_page": 40,
    "order": "publish_date+desc%2Ccreated_at+desc",
    # "search": ,
    "category": "19%2C165%2C184%2C204",
    "blank_scope": "Latest",
}

# r_nmn = requests.get(URL)
r_nmn = requests.get(URL_NMN, params = BASE_PARAMS_NMN)

# print(r_nmn.status_code)
# print(r_nmn.text)

soup_nmn = BeautifulSoup(r_nmn.text, "html.parser")
# print(soup_nmn.prettify())
# print(soup_nmn.find(class_="content_title").text.strip())
titles = soup_nmn.find_all(class_="content_title")
title = titles[0].text.strip()
# print(title)
# print(soup_nmn.find(class_="content_title").find_all("p").text.strip())
# print(soup_nmn.find(class_="article_teaser_body"))
texts = soup_nmn.find_all("p")
text = texts[0].text
# print(text)



# JPL Mars Space Images - Featured Image
## I don't know what splinter is??


# Mars Facts
BASE_URL_MF = "https://space-facts.com/mars/"

r_mf = requests.get(BASE_URL_MF)
# print(r_mf.status_code)

soup_mf = BeautifulSoup(r_mf.text, "html.parser")
# print(soup_mf)
# table = soup_mf.find("section", class_ = "sidebar widget-area clearfix").find("tablepress tablepress-id-p-mars")
# table = soup_mf.find("div", class_ = "textwidget")
table = soup_mf.find("table", class_ = "tablepress tablepress-id-p-mars")
# print(table.prettify())

## This doesn't work
# df_mf = pd.read_html(table)
# print(df_mf)



# Mars Hemispheres
BASE_URL_MH = "https://astrogeology.usgs.gov/search/results"
BASE_PARAMS_NH = {
    "q": "hemisphere+enhanced",
    "k1": "target",
    "v1": "Mars",
}

r_mh = requests.get(BASE_URL_MH, params = BASE_URL_MH)
# print(r_mh.status_code)

soup_mh = BeautifulSoup(r_mh.text, "html.parser")
# print(soup_mh.prettify())

# images = soup_mh.find_all("div", class_ = "result-list")
# images = soup_mh.find_all("div", class_ = "item")
# image = images[0]
# image = images.find("div", class_ = "item").find("img")["src"]

images = soup_mh.find("div", class_ = "item")
print(images.prettify())
# print(image.prettify())