"""
To see an example of the Wikipedia API JSON look at this url:
https://en.wikipedia.org/api/rest_v1/page/summary/Japanese_cuisine
"""
import requests

def get_wiki(title): 
	url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
	req = requests.get(url)
	if req.status_code != 200:
		print(f"We got an error: {req.status_code}")
		exit()
	return req

def get_data(value):
	data = get_wiki(title).json()
	if value == "both":
		return (data["extract"]) + (data["description"])
	else:
		return (data[value])

def get_url(url_ask):
	if url_ask == "yes":
		print(f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}")
	else:
		print("alright no title")

title = input("wich page do you want to visit?").strip().lower()
value_ask = input("Do you want the extract, description or both?").strip().lower()
url_ask = input("do you want to get the url?").strip().lower()
wiki = get_data(value_ask)
print(wiki)
get_url(url_ask)