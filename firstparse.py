import requests
from bs4 import BeautifulSoup

# url = "https://napodrabotku.ru/jobs-freelancers/marketing?page=2"

# headers ={
#      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 "
#  }

# req=requests.get(url, headers=headers)
# src=req.text
# print(src)

# with open("index.html", "w", encoding="utf-8") as file:
#            file.write(src)

with open("index.html", "r", encoding="utf-8") as file:
    src=file.read()

soup=BeautifulSoup(src, "lxml")

all_products = soup.find_all(class_="category-orders__list-item")
for item in all_products:
        item_title=item.find(class_="category-orders__list-item-title").text
        item_midle=item.find(class_="category-orders__list-item-link")
        item_href=item_midle.get("href")

        print(f"{item_title}: {item_href}")
        
        # print(item)