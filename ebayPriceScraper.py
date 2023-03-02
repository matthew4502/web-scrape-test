#Matthew E. Test Webscraper
import requests #Used to get inspection data
from bs4 import BeautifulSoup #Used to parse the inspection data


URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499337.m570.l1313&_nkw=pencil&_sacat=0"
page = requests.get(URL) #Pull the element data
#print(page.text) #Output the element data

soup = BeautifulSoup(page.content, "lxml")

prices = soup.find_all("span", attrs={'class':'s-item__price'})

priceList = []
for price in prices:
    priceSTR = str(price.text)
    priceSTR = priceSTR.replace("$", '')
    priceSTR = priceSTR.replace(" to ", " ")
    if " " in priceSTR:
        i = 0
        for c in priceSTR:
            if priceSTR[i].isspace():
                print("Found a double val")
                print(priceSTR[0:i])
                print(priceSTR[i:])
                priceList.append(priceSTR[0:i])
                priceList.append(priceSTR[i:])
                break
    else:
        priceList.append(priceSTR)

for val in priceList:
    print(val)