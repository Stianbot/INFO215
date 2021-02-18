from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def get_urls(url):
    url_list = []
    open_url = urlopen(url)
    bs = BeautifulSoup(open_url, 'html.parser')

    x = bs.find(id="mw-content-text").find(class_='div-col').find_all('a')
    for a in x:
        url_list.append(a.attrs['href'])

    return url_list


def definitive_link(list_of_links, url):
    full_url_list = []
    for link in list_of_links:
        full_url_list.append(urljoin(url, link))

    return full_url_list


def get_header(url):
    open_url = urlopen(url)
    bso = BeautifulSoup(open_url, 'html.parser')
    y = bso.find('h1').get_text()
    return y
