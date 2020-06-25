import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=266' # url tempat melakukan scraping
contents = requests.get(url)
# print(contents.text)
response = bs4.BeautifulSoup(contents.text, "html.parser")
# bs4 = package, beautifulsoup = class, contents.text = suply contenst yg berisi request yg mengambil url dari web
data = response.find_all('tr','table_highlight')
data = data[0]  # untuk menghilangkan kurung kurawal, agar data di mulai dari data ke 0

sholat = {} # inisialisasi bahwa sholat merupakan dictionary, yg memiliki nama variabel yang memiliki
            # attribute jam sholatnya
i = 0
for d in data:
    if i == 1: # kenapa di deklarasikan data ke 1, karena data ke 0 = tanggalnya
        sholat['shubuh'] = d.get_text()
    elif i == 2:
        sholat['dhuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1
print(sholat)
print(sholat['ashar'])