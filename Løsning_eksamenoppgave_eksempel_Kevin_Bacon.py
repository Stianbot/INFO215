from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
open_url = urlopen(url)
bs = BeautifulSoup(open_url, "html.parser")

links = []

for link in bs.find_all('a', {"href": re.compile("^(/wiki/)(?!File|Category|Template|Special|Wikipedia|Help|Portal|Talk|(.*identifier)|Main_Page)")}):
    links.append(urljoin(url, link.attrs['href']))

links = list(set(links))

for webpage in links[:]:
    ol = urlopen(webpage)
    page = BeautifulSoup(ol, "html.parser")

    try:
        table = page.find("table", class_="infobox vevent")
        th = table.find("th", class_="infobox-label")
        text = th.get_text()

        if text == "Directed by":
            director = table.find("td", class_="infobox-data").get_text()
            title = page.h1.text
            print(f"Title: {title}, Director: {director}")

    except:
        continue

