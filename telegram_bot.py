import time

import requests


bot_token ="7924417613:AAHW0j-EMKTeeaBsVlUJk425fQMlFZCqStk"
#usx = "https://api.telegram.org/bot7924417613:AAHW0j-EMKTeeaBsVlUJk425fQMlFZCqStk/sendMessage?chat_id=5177622824&text=Hello%20from%20my%20Python%20bot!"
user_id ="5177622824"

message ="hello dinesh,this runs sucessfully"


url =f'https://api.telegram.org/bot{bot_token}/sendMessage'

params= {
           'chat_id': user_id,
           'text': message
    }
response=requests.get(url,params=params)

if response.status_code ==200:
    print(f"massage sent : {message}")
else:
    print("massage failed")