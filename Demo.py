file = open("spacex.txt", "r")
data = file.read()
file.close()
reply = data.replace('dine','raki')
dine = open("spacex.txt","w+")
line = dine.readline()
dine.write(reply)
dine.close()

print(reply)


