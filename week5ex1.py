#asking for the URL
url = input("What url would you like to scrape?")
url = url.strip()
import requests

#getting the status code and give error if not 200
r = requests.get(url)
print(r.status_code)
if r.status_code != 200:
	print("The scraping did not work, programm will now exit")
	exit()

#getting all headers and displaying them in a list
all_headers = r.headers
for key, value in all_headers.items():
	print(f"{key} : {value}")

#getting the text and displaying the first 10 lines
all_text = r.text
index = 0

while index < 10:
	line = all_text.splitlines()[index]
	print(line)
	index = index + 1
