import time

import requests
import csv
from bs4 import BeautifulSoup
import lxml
from flask import url_for
from urllib3 import request

url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_2_3_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_2_3_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=mobiles&requestId=eb4409f8-9e82-4fb3-a4f1-843a95724899"
time.sleep(5)
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    print("connection sucessfully")
    html_content = response.text

    soup = BeautifulSoup(html_content, 'lxml')
    # print(soup.prettify())

    flip_data = soup.find_all('div', class_="_75nlfW")
    # print(flip_data)
    with open('flip_data.csv', 'w', newline='', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['mobiles_types', 'features', 'prices', 'rating', 'review', 'links'])

        for flip in flip_data:
            mobile = flip.find('div', class_="KzDlHZ").text
            feature = flip.find('ul', class_="G4BRas").text
            price = flip.find('div', class_="Nx9bqj _4b5DiR").text
            rating = flip.find('div', class_="XQDdHH").text
            review = flip.find('span', class_="Wphh3N").text
            link = flip.find('a', href=True).get('href')
            writer.writerow([mobile, feature, price, rating, review, link])

            print(mobile)
            print(feature)
            print(price)
            print(rating)
            print(review)
            print(link)
            print('#' * 10)

else:
    print(f"connection error{response.status_code}")
