wrongwords = ["kut", "gvd", "nee", "ja", "omg", "facebook", "arjen"]
zin = input("schrijf eens een leuke zin")

zinlijst = zin.split()
for zincheck in zinlijst:
	if zincheck in wrongwords:
		print("dat mag je niet gebruiken")
