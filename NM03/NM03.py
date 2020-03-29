import string

X = "EG GM GB GH DK CA ED GB HE FP EJ GO FP FE GI GF FP EE GB HE CB".split(" ")

L = string.ascii_uppercase[:16]

x = 0

D = {}

for i in L:
    for j in L:
        D[i+j] = chr(x % 255)
        x+=1

for x in X:
    print(D[x],end="")

print("")
