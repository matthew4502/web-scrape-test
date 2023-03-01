#Matthew E. Test Webscraper
import requests #Used to get inspection data
from bs4 import BeautifulSoup #Used to parse the inspection data


URL = "https://www.amazon.com/s?k=pencil&crid=3SCD4ABA737Q9&sprefix=pencil%2Caps%2C148&ref=nb_sb_noss_1"
page = requests.get(URL) #Pull the element data
#print(page.text) #Output the element data

soup = BeautifulSoup(page.content, "lxml")

prices = soup.find_all("span", attrs={'class':'a-offscreen'})

for price in prices:
    print(price.text)
