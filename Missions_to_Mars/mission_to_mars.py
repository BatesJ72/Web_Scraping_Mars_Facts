import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Selenium
def get_html(url, wait):
    # fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    # driver = webdriver.Firefox(firefox_options = fireFoxOptions)
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()
    return html


# NASA Mars News

def get_html_nmn(url_nmn, wait):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()
    return html_nmn


# url_nmn = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# html_nmn = get_html(url_nmn, wait = 1)
# soup_nmn = BeautifulSoup(html_nmn, "html.parser")

# titles = soup_nmn.find_all("div", class_="content_title")
# news_title = titles[1].text.strip()
# print(news_title)

# texts = soup_nmn.find_all("div", class_="article_teaser_body")
# news_p = texts[0].text
# print(news_p)



# JPL Mars Space Images - Featured Image

def get_html_jpl(url_jpl, wait):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()
    return html_jpl

url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
html_jpl = get_html(url_jpl, wait = 1)
soup_jpl = BeautifulSoup(html_jpl, "html.parser")

# image = soup_jpl.find("div", class_ = "image_and_description_container").find("div").find("img")["src"]
image = soup_jpl.find("div", class_ = "img").find("img")["src"]
print(image)





# # Mars Facts
# BASE_URL_MF = "https://space-facts.com/mars/"

# r_mf = requests.get(BASE_URL_MF)
# # print(r_mf.status_code)

# soup_mf = BeautifulSoup(r_mf.text, "html.parser")
# # print(soup_mf)
# # table = soup_mf.find("section", class_ = "sidebar widget-area clearfix").find("tablepress tablepress-id-p-mars")
# # table = soup_mf.find("div", class_ = "textwidget")
# table = soup_mf.find("table", class_ = "tablepress tablepress-id-p-mars")
# # print(table.prettify())

# ## This doesn't work
# # df_mf = pd.read_html(table)
# # print(df_mf)



# # Mars Hemispheres
# BASE_URL_MH = "https://astrogeology.usgs.gov/search/results"
# BASE_PARAMS_NH = {
#     "q": "hemisphere+enhanced",
#     "k1": "target",
#     "v1": "Mars",
# }

# r_mh = requests.get(BASE_URL_MH, params = BASE_URL_MH)
# # print(r_mh.status_code)
# # print(r_mh.text)

# soup_mh = BeautifulSoup(r_mh.text, "html.parser")
# # print(soup_mh.prettify())

# # images = soup_mh.find_all("div", class_ = "result-list")
# # images = soup_mh.find_all("div", class_ = "item")
# # image = images[0]
# # image = images.find("div", class_ = "item").find("img")["src"]

# images = soup_mh.find("div", class_ = "item")
# # print(images.prettify())
# # print(image.prettify())