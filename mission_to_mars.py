#!/usr/bin/env python
# coding: utf-8

# ### ---------------------------------------------
# ## Web Scraping - Mission to Mars
# ### ---------------------------------------------

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# URL of pages to be scraped
mars_news_url = 'https://redplanetscience.com'
space_img_url = "https://spaceimages-mars.com"
mars_facts_url = "https://galaxyfacts-mars.com"
hemisph_url = "https://marshemispheres.com"

# Setup Splinter Browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News

# Go to the news url
browser.visit(mars_news_url)

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Find the news section
latest_news = soup.find('div', id='news')

# Get the latest news title
news_title = latest_news.find('div', class_='content_title').text
news_title

# Get the latest news paragraph
news_p = latest_news.find('div', class_='article_teaser_body').text
news_p


# ### JPL Mars Space Images - Featured Image

# Visit the url for the Featured Space Image site 
browser.visit(space_img_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Find the image complete url for the current Featured Mars Image full size
local_image_url = soup.find('img', class_="headerimage fade-in")['src']
featured_image_url = space_img_url+'/'+local_image_url
featured_image_url

# ### Mars Facts

# Via Pandas scrape the table containing facts about the planet
tables = pd.read_html(mars_facts_url)
tables

# Save data frame for needed table
df = tables[0]
df

# Rename columns, drop first row and set index
df.rename(columns = {0:'Facts', 1:'Mars', 2:'Earth'}, inplace=True)
df.drop(0, inplace=True)
df.set_index('Facts', inplace=True)
df

# Convert the data to a HTML table string
html_table = df.to_html()
html_table.replace('\n', '')
html_table

# ### Mars Hemispheres

browser.visit(hemisph_url)

# Find link texts to go to each hemisphere url  
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
 
links_text = []
items = soup.find_all('div', class_='item')
for it in items:
    descr = it.find('div', class_='description')
    links_text.append(descr.find('h3').text)
links_text

# Find links to full size images of mars hemispheres

# Define list to add title and img url for each hemisphere
hem_img_ttl_urls = []

# Loop through the hemisphere links to click on them and get title and url values
for txt in links_text:
    
    # Save title of the hemisphere  
    title = txt.replace(" Enhanced","")
    
    # Click hemisphere to access link to the original image
    browser.links.find_by_partial_text(txt).click()
    
    # Use Beautiful Soup to find the link
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = hemisph_url+'/'+soup.find('a', text = 'Original')['href']
    
    # Add to the list of dictionaries
    hem_img_ttl_urls.append({"title": title, "img_url": img_url})
    
    # Return to the main page
    browser.links.find_by_partial_text("Back").click()

hem_img_ttl_urls


browser.quit()

final_dict = {'news_title': news_title, 'news_par': news_p, "featured_img": featured_image_url,
           "table": html_table, "hemispheres": hem_img_ttl_urls}
print(final_dict)


