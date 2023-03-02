#Matthew E. Test Webscraper
import requests #Used to get inspection data
from bs4 import BeautifulSoup #Used to parse the inspection data
import numpy #Used to analayze data
from scipy import stats #Used for analyzing mode

reqItem = input("What would you like to know the pricing information on?\n")#Take input on what to parse information on
print("")
str(reqItem)#Change the input into a string class
reqItem = reqItem.replace(" ", "+")#replace any blank space with a + to conform with ebay searches that have multiple words
URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499337.m570.l1313&_nkw=" + reqItem +"&_sacat=0"#create the URL of the ebay search
page = requests.get(URL) #Pull the element data
#print(page.text) #Output the element data

soup = BeautifulSoup(page.content, "lxml")#Set up the parser

prices = soup.find_all("span", attrs={'class':'s-item__price'})#Find all instances of item  pricing

#doubleCount = 0 #Used for testing
#singleCount = 0 #Used for testing
priceList = []#set up a list of prices after reformatting the data
for price in prices:
    priceSTR = str(price.text)#Pull the data out of each price line in the html
    priceSTR = priceSTR.replace("$", '')#Remove the $ from the data
    priceSTR = priceSTR.replace(" to ", " ")#Change the format of separator for ranging prices
    #Note: Ranging prices are of the form "$Price to $Price"
    #All prices will be converted to floats when added to the priceList in order to perform calculations later
    #and will be formatted with two decimal points since they are a price
    if " " in priceSTR:#If there was a ranging price
        i = 0
        for c in range(len(priceSTR)):#Check until we find the ranging price
            if priceSTR[i].isspace():
                #Testing if properly sensing and separating ranging prices
                #print("Before")
                #print("Found a double val")
                #print(priceSTR[0:i])
                #print(priceSTR[i+1:])
                #print("After")
                #After tests add values
                priceList.append(round(float(priceSTR[0:i]), 2))#Add the first price
                priceList.append(round(float(priceSTR[i+1:]), 2))#Add the second price
                #doubleCount = doubleCount + 1 #Used for testing
                break
            i = i + 1
    else:
        priceList.append(round(float(priceSTR), 2))
        #singleCount = singleCount + 1 #Used for testing

#Sort the list so output can be least to greatest
priceList.sort()

print("All values found from lowest to highest price:")
for val in priceList:
    print("$",val)

#Now we will analyze the data, with all values rounded to two decimal points since they are prices
stdDev = round(numpy.std(priceList), 2)
mean = round(numpy.mean(priceList), 2)
mode = stats.mode(priceList)
median = round(numpy.median(priceList), 2)
range = round((priceList[len(priceList) - 1] - priceList[0]) + 0.00, 2)
print("Statistics on found pricing data:")
print("Mean: $",mean)
print("Median: $",median)
print("Mode: $",mode)
print("Range: $",range)
print("Standard Deviation: $",stdDev)

#print("There were ", doubleCount, " ranging prices")#Used for testing
#print("There were ", singleCount, " regular prices")#Used for testing