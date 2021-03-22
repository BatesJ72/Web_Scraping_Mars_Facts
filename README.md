Web Scraping - Mission to Mars

I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. I completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Selenium.

I scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. I used splinter to navigate the site and find the image url for the current Featured Mars Image.I included high resolution images for each of Mar's hemispheres from the USGS Astrogeology site. I then used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped.
