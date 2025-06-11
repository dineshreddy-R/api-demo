
file =open('spacex.txt','r+')
data= file.read()
words = data.split()
print(f"total data = {words}\n",len(words))