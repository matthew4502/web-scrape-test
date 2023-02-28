#Matthew E. Test Webscraper
import requests #Used to get inspection data
from bs4 import BeautifulSoup #Used to parse the inspection data


URL = "https://toscrape.com/"
page = requests.get(URL) #Pull the element data
#print(page.text) #Output the element data

#Define my soup instance as an html parser for the contents of the page I pulled
soup = BeautifulSoup(page.content, 'html.parser')

#Find the container class in the html code for the site
container = soup.find(class_="container")
#print(container.prettify()) #Print all html inside the container element
#prettify() just makes the output easier to read by adding proper tabbing

#Find all row class instances inside the container class
containerClasses = container.find_all(class_="row")
#for c in containerClasses:
#    print(c.prettify())

#Print all of the html code for each of the row classes in the container class
links = soup.find_all("a")
for link in links:
    link_urle = link["href"]
    print(link_urle)
