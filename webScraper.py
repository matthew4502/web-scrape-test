#Matthew E. Test Webscraper
import requests #Used to get inspection data
from bs4 import BeautifulSoup #Used to parse the inspection data


URL = "https://www.samsung.com/us/"
page = requests.get(URL) #Pull the element data
print(page.text) #Output the element data

#Define my soup instance as an html parser for the contents of the page I pulled
soup = (page.content, 'html.parser')

rows = soup.select('class=')['nv00-gnb__featured-products-thumbnail-item-name']