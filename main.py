import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=266' # url tempat melakukan scraping
contents = requests.get(url)
# print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
# bs4 = package, beautifulsoup = class, contents.text = suply contenst yg berisi request yg mengambil url dari web

print(response)