X = "ab a2 a1 a1 a2 ba 92 b9 a5 a8 92 b5 a2 bf 92 af bf a4 ae a6 92 bf a2 ac a9"

for i in range(255):
	Y = "".join([chr(int(x,16)^i) for x in X.split(" ")])

	if "_" in Y:
		print(Y)