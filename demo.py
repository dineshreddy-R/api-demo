import requests


def main():
    '''with open("spacex.txt","w") as file:
        v=file.write("Raki\nraju,\ndine\nparthu")'''

    '''with open("spacex.txt","r") as file:
        v = file.readlines()'''

    '''A=int(input("enter the number: "))
    B = int(input("enter the divid number: "))
    c = A**B
    print("the result is:",c)'''

    '''tuple = (1,2,3,2,4,4,5,4,6,5,7,6)
    d=tup.count(4)
    v=tup.index(4)
    print(d,v)
    '''

    '''dict = {"dine":"raki","age":22,"branch":"ece"}
    new=set((dict))
    print(new)'''

    '''my_tuple =tuple((x for x in range(4)))
    print(my_tuple)'''
    '''my_set = set()
    my_set.add(10)
    my_set.add(20)'''

    '''dit={'name':'dine','age':22,'city':'ctr'}
    for key,value in dit.items():
        print(key,":" ,value)'''

    bot_token = "7924417613:AAHW0j-EMKTeeaBsVlUJk425fQMlFZCqStk"

    user_id = "5177622824"
    message = "dineshreddy"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "user": user_id,
        "text": message
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("sucess")
    else:
        print("fail")


if __name__ == "__main__":
    main()
