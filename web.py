import requests
from bs4 import BeautifulSoup
import csv
import lxml

url = "https://www.booking.com/searchresults.en-gb.html?ss=Bengaluru&ssne=Bengaluru&ssne_untouched=Bengaluru&efdco=1&label=in-bangalore-gCKRuFuSqOmaboZFplLW*QS453829303834%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-302351225471%3Alp9062082%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGgfEoJVv7zYo&sid=15a3f072894980849974b019a3801b9d&aid=1610687&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2090174&dest_type=city&checkin=2025-06-06&checkout=2025-06-07&group_adults=2&no_rooms=1&group_children=0"
header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

response = requests.get(url,headers=header)
print(response.status_code)

if response.status_code==200:
    print("connected to website")
    html_content = response.text

    soup = BeautifulSoup(html_content,'lxml')
    #print(soup.prettify())

    #main container
    hotals= soup.find_all('div',role="listitem")
    #print(hotals)

    for hotal in hotals:
        hotal_name=hotal.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip()
        location = hotal.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
        price = hotal.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.strip()
        room = hotal.find('h4',class_="fff1944c52 f254df5361").text.strip()
        #review = hotal.find('div',class_="f63b14ab7a f546354b44 becbee2f63")




        print(hotal_name)
        #print('@'*1)
        print(location)
        #print('!'*2)
        print(price)

        print(room)
        #the doubt of review
       # print(review)
        print('$'*5)



else:
    print(f"connection failed{response.status_code}")