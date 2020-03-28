X = ["SRUE",
     "SRAU",
     "SRC",
     "SRUEC",
     "SRPEC",
     "SPAUEC",
     "SRU",
     "SRAUEC",
     "SRAUE",
     "SRPU",
     "SPAUEC",
     "SRAU",
     "SRAC",
     "SRPUE",
     "SRUC",
     "SPAUEC",
     "SRA",
     "SRUC",
     "SRPE",
     "SRUC",
     "SPAUEC",
     "SRPEC",
     "SRUC",
     "SRAUC",
     "SRC",
     "SRP",
     "SRA",
     "SRAUEC",
     "SRPE",
     "SRUC"]

count = 0;

Y = {}

for a in ["","S"]:
    for b in ["","R"]:
        for c in ["","P"]:
            for d in ["","A"]:
                for e in ["","U"]:
                    for f in ["","E"]:
                        for g in ["","C"]:

                            Y[a+b+c+d+e+f+g] = count

                            count+=1

for x in X:
    print(chr(Y[x]),end="")