from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re


def get_webpage(url):
    request = urlopen(url)
    bs = BeautifulSoup(request, 'html.parser')
    return bs


def get_links(bs, base):
    full_links = []
    for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            full_links.append(urljoin(base, link.attrs['href']))
    return full_links


def print_links(link):
    for li in link:
        print(li)


def get_images(bs, base):
    full_links = []
    for img in bs.find_all('img', src=re.compile('^(//upload.wikimedia.org)')):
        full_links.append(urljoin(base, img.attrs['src']))
    return full_links


