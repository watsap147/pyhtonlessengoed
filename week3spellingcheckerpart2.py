wrongwords = ["kut", "gvd", "nee", "ja", "omg", "facebook", "arjen"]
goeieworden = ["jammer", "helaas", "misschien", "wel", "umg", "twitter", "naam"]
zin = input("schrijf eens een leuke zin")

index = 0
woorden = zin.split()
for woord in woorden:
	if woord in wrongwords:
		goeie_woord_index = wrongwords.index(woord)
		woorden[index] = goeieworden[goeie_woord_index]
	index = index + 1
woorden = " ".join(woorden)
print(woorden)

