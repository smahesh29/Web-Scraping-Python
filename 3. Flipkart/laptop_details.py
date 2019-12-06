from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"C:\Users\Mahesh Sawant\Desktop\Web Scraping\Project\chromedriver_win32\chromedriver.exe") #Set the path to chromedriver

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content)
all_laptops = soup.findAll('a',href=True, attrs={'class':'_31qSD5'})

for laptop in all_laptops:
    name=laptop.find('div', attrs={'class':'_3wU53n'})
    price=laptop.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=laptop.find('div', attrs={'class':'hGSR34'})
    products.append(name.text.strip())
    prices.append(price.text.strip())
    ratings.append(rating.text.strip()) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('laptop_details.csv', index=False, encoding='utf-8')