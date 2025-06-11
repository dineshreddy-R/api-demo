import requests
from bs4 import BeautifulSoup
import csv
import lxml

url = 'https://www.coldwellbankerhomes.com/tx/dallas/agents'

response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    print('connected sucessfully')

    with open('coldwell.html', 'wb') as file:
        file.write(response.content)

    html_content = response.text
else:
    print("failed", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

cold_data = soup.find_all('div', class_="agent-block col")

for cold in cold_data:
    name = cold.find('h2',class_="agent-content-name notranslate").text.strip()
    phone = cold.find('a',class_="phone-link").text.strip()


    print(name)
    print(phone)
    print('$'*10)
