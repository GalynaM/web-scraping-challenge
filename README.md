# web-scraping-challenge

This project builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Step1
Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
* mission_to_mars.ipynb - Jupyter Notebook that completes all of the scraping and analysis tasks:
- get the latest mars news and paragraph
- get the Featured Space Image
- via Pandas scrape the table with planet facts
- obtain high resolution images for each of Mar's hemispheres.
URL used:
'https://redplanetscience.com'
"https://spaceimages-mars.com"
"https://galaxyfacts-mars.com"
"https://marshemispheres.com"

Step2
Using MongoDB with Flask templating a new HTML page created that displays all of the information that was scraped from the URLs above.
* scrape_mars.py - Python script with a function called scrape that executes all of the scraping code and returns one Python dictionary containing all of the scraped data
* app.py - Python script to create web application that scrapes data and saves/reads it in Mongo db, Flask and Pymongo used.
* templates->index.html - template HTML file that takes the mars data dictionary and displays all of the data in the appropriate HTML elements, Bootstrap, Jinja2.
* static->style.css - SCC file with styles for index.html

Missions_to_Mars - is the project folder.
Output - is the folder with application screenshots.
