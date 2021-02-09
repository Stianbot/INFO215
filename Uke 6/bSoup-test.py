'''

Eksport av Jupyter notebook. Anbefales å kjøre denne koden jn slik at det ikke sendes ut så mange requests
til Wikipedia. Etter at in[2] er kjørt så er hele nettsiden lagret i variabelen: bs.

'''
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re


# In[2]:


# parser url slik at de ulike delene av url-en kan brukes senere.
url = urlparse('https://en.wikipedia.org/wiki/Apollo_14')

html = urlopen('https://en.wikipedia.org/wiki/Apollo_14')

# Lager nettsiden om til BeautifulSoup-objekt. Hele nettsiden er "fanget" i bs variabelen.
bs = BeautifulSoup(html,'html.parser')


# In[3]:


# Nettsiden kan navigeres med dot-notering. .get_text() brukes for å skrive ut tekstinnholdet uten html-tags.
# Skriver ut første overskrift på nettsiden.
print(bs.h1.get_text())


# In[4]:


#.find_all() fungerer som et søk på nettsiden. Den går gjennom hele siden og leter etter det du har spesifisert at den skal finne.
# Her finner den alle p-tags og skriver ut tekstinnholdet i paragrafene.
paragraf_liste = bs.find_all('p')
for tekst in paragraf_liste:
    print(tekst.get_text())


# In[11]:


# Løkke som henter ut alle a tags som har href likt regex-utrykket: '^(/wiki/)'. Dette representerer interne wikipedia-linker.
# Det blir ikke gjort fullstendig utsortering av linker, så det kommer med ting som er uønsket.
# Det mangler også at disse gjøres til fullverdige linker som kan klikkes på.
for link in bs.find_all('a', {"href": re.compile('^(/wiki/)')}):
    print(link['href'])


# In[12]:


# Gjør samme som over, men med annet syntaks i .find_all()
for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
    print(link['href'])

