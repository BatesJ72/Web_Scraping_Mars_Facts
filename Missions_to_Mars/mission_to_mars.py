import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



# Selenium
# def get_html(url, wait):
#     # fireFoxOptions = webdriver.FirefoxOptions()
#     # fireFoxOptions.set_headless()
#     # driver = webdriver.Firefox(firefox_options = fireFoxOptions)
#     driver = webdriver.Firefox()
#     driver.get(url)
#     driver.implicitly_wait(wait)
#     html = driver.page_source
#     driver.close()
#     return html


# NASA Mars News

# def get_html_nmn(url_nmn, wait):
#     driver = webdriver.Firefox()
#     driver.get(url_nmn)
#     driver.implicitly_wait(wait)
#     html_nmn = driver.page_source
#     driver.close()
#     return html_nmn


# url_nmn = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# html_nmn = get_html_nmn(url_nmn, wait = 1)
# soup_nmn = BeautifulSoup(html_nmn, "html.parser")

# titles = soup_nmn.find_all("div", class_="content_title")
# news_title = titles[1].text.strip()
# print(news_title)

# texts = soup_nmn.find_all("div", class_="article_teaser_body")
# news_p = texts[0].text
# print(news_p)



# JPL Mars Space Images - Featured Image

# def get_html_jpl(url_jpl, wait):
#     driver = webdriver.Firefox()
#     driver.get(url_jpl)
#     driver.implicitly_wait(wait)
#     html_jpl = driver.page_source
#     driver.close()
#     return html_jpl

# url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# html_jpl = get_html_jpl(url_jpl, wait = 1)
# soup_jpl = BeautifulSoup(html_jpl, "html.parser")

# image = soup_jpl.find("div", class_ = "img").find("img")["src"]
# print(image)





# # Mars Facts

# def get_html_mf(url_mf, wait):
#     driver = webdriver.Firefox()
#     driver.get(url_mf)
#     driver.implicitly_wait(wait)
#     html_mf = driver.page_source
#     driver.close()
#     return html_mf

# url_mf = "https://space-facts.com/mars/"
# html_mf = get_html_mf(url_mf, wait = 1)
# soup_mf = BeautifulSoup(html_mf, "html.parser")
# # print(soup_mf.prettify())

# table_mf = soup_mf.find("table", class_ = "tablepress tablepress-id-p-mars")
# # print(table_mf.prettify())

# with open('mars_facts_table.html', 'w+', encoding = 'utf-8') as f:
#     f.write(str(table_mf))



# Mars Hemispheres

# Image 1

def get_html_mh(url_mh, wait):
    driver = webdriver.Firefox()
    driver.get(url_mh)
    driver.implicitly_wait(wait)
    html_mh = driver.page_source
    driver.close()
    return html_mh

url_mh = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
html_mh = get_html_mh(url_mh, wait = 1)
soup_mh = BeautifulSoup(html_mh, "html.parser")
# print(soup_mh.prettify())

image = soup_mh.find("div", class_ = "downloads").find("a")["href"]
# print(image.prettify())
print(image)