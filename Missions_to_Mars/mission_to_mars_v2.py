import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import os
import pymongo
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars



def scrape():
    # NASA Mars News

    def get_html_nmn(url_nmn, wait):
        driver = webdriver.Firefox()
        driver.get(url_nmn)
        driver.implicitly_wait(wait)
        html_nmn = driver.page_source
        driver.close()
        return html_nmn


    url_nmn = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    html_nmn = get_html_nmn(url_nmn, wait = 1)
    soup_nmn = BeautifulSoup(html_nmn, "html.parser")

    titles = soup_nmn.find_all("div", class_="content_title")
    news_title = titles[1].text.strip()
    # print(news_title)

    texts = soup_nmn.find_all("div", class_="article_teaser_body")
    news_p = texts[0].text
    # print(news_p)


    # JPL Mars Space Images - Featured Image

    def get_html_jpl(url_jpl, wait):
        driver = webdriver.Firefox()
        driver.get(url_jpl)
        driver.implicitly_wait(wait)
        html_jpl = driver.page_source
        driver.close()
        return html_jpl

    url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    html_jpl = get_html_jpl(url_jpl, wait = 5)
    soup_jpl = BeautifulSoup(html_jpl, "lxml")

    img_jpl = soup_jpl.find('article')['style'].replace('background-image: url(', '').replace(');', '')[1:-1]
    img_jpl_final = "https://www.jpl.nasa.gov/" + img_jpl


    # Mars Facts

    def get_html_mf(url_mf, wait):
        driver = webdriver.Firefox()
        driver.get(url_mf)
        driver.implicitly_wait(wait)
        html_mf = driver.page_source
        driver.close()
        return html_mf

    url_mf = "https://space-facts.com/mars/"
    html_mf = get_html_mf(url_mf, wait = 1)
    soup_mf = BeautifulSoup(html_mf, "html.parser")

    table_mf = soup_mf.find("table", class_ = "tablepress tablepress-id-p-mars")


    # Mars Hemispheres

    # Image 1

    def get_html_mh1(url_mh1, wait):
        driver = webdriver.Firefox()
        driver.get(url_mh1)
        driver.implicitly_wait(wait)
        html_mh1 = driver.page_source
        driver.close()
        return html_mh1

    url_mh1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    html_mh1 = get_html_mh1(url_mh1, wait = 1)
    soup_mh1 = BeautifulSoup(html_mh1, "html.parser")
    image_mh1 = soup_mh1.find("div", class_ = "downloads").find("a")["href"]


    # Image 2

    def get_html_mh2(url_mh2, wait):
        driver = webdriver.Firefox()
        driver.get(url_mh2)
        driver.implicitly_wait(wait)
        html_mh2 = driver.page_source
        driver.close()
        return html_mh2

    url_mh2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    html_mh2 = get_html_mh2(url_mh2, wait = 1)
    soup_mh2 = BeautifulSoup(html_mh2, "html.parser")
    image_mh2 = soup_mh2.find("div", class_ = "downloads").find("a")["href"]


    # Image 3

    def get_html_mh3(url_mh3, wait):
        driver = webdriver.Firefox()
        driver.get(url_mh3)
        driver.implicitly_wait(wait)
        html_mh3 = driver.page_source
        driver.close()
        return html_mh3

    url_mh3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    html_mh3 = get_html_mh3(url_mh3, wait = 1)
    soup_mh3 = BeautifulSoup(html_mh3, "html.parser")
    image_mh3 = soup_mh3.find("div", class_ = "downloads").find("a")["href"]


    # Image 4

    def get_html_mh4(url_mh4, wait):
        driver = webdriver.Firefox()
        driver.get(url_mh4)
        driver.implicitly_wait(wait)
        html_mh4 = driver.page_source
        driver.close()
        return html_mh4

    url_mh4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    html_mh4 = get_html_mh4(url_mh4, wait = 1)
    soup_mh4 = BeautifulSoup(html_mh4, "html.parser")
    image_mh4 = soup_mh4.find("div", class_ = "downloads").find("a")["href"]


    # Image Dictionary

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "image_mh1"},
        {"title": "Schiaparelli Hemisphere", "img_url": "image_mh2"},
        {"title": "Syrtis Major Hemisphere", "img_url": "image_mh3"},
        {"title": "Valles Marineris Hemisphere", "img_url": "image_mh4"},
    ]

    # print(hemisphere_image_urls)

    # Create Dictionary for All Data
    mars_data = {}
    
    mars_data.update({"title1": "news_title", "url1": news_title})
    mars_data.update({"title2": "news_paragraph", "url2": news_p})
    mars_data.update({"title3": "Cerberus Hemisphere", "url3": image_mh1})
    mars_data.update({"title4": "Schiaparelli Hemisphere", "url4": image_mh2})
    mars_data.update({"title5": "Syrtis Major Hemisphere", "url5": image_mh3})
    mars_data.update({"title6": "Valles Marineris Hemisphere", "url6": image_mh4})
    mars_data.update({"title7": "mars_fact_table", "url7": table_mf})
    mars_data.update({"title8": "background_image", "url8": img_jpl_final})
    
    
    return mars_data
