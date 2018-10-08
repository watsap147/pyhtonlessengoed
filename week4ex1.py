#creat dictonary
movie = {
	"title" : "django unchained",
	"year" : 2012,
	"duration" : 154,
	"director" : "Quentin Tarantino"
}
#create actors
movie["actors"] = ["jammie foxx", "leonardo dicapario", "samuel l jackson"]

#loop dictonary
for key, value in movie.items():
	#look for duration
	if key == "duration":
		print(f"{key} : {value} minutes")
	#look for actor list
	elif key == "actors":
		print(key + " : " + ",".join(value))
	#print rest of the list
	else:
		print(f"{key} : {value}")


