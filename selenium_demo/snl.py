# Husk å installere selenium: pip install selenium.
# Husk at du trenger en webdriver for å kjøre denne koden.
from selenium import webdriver
import random
import os.path
from os import path

url = 'https://snl.no/'  # Nettsiden som ønskes besøkt.

'''
Jeg bruker en firefox webdriver "geckodriver".
Denne koden går ut i fra at driveren (geckodriver.exe)
ligger på samme nivå som denne filen, i mappehirearkiet.
Om dette ikke er tilfelle hos deg så må pathen til driveren skrives inn
som et argument i parantesene () på linje 16. dette skrives inn som
"executable_path=**PATH/TO/DRIVER**". Det enkleste er å ha den på samme nivå.
'''
driver = webdriver.Firefox()
driver.get(url)  # Henter nettsiden


# Finner lenken til artikkelen, som er forside-artikkelen på siden. (stort bilde)
cover_page_url = driver.find_element_by_class_name('hero-image__link').get_attribute('href')

# Henter ny side.
driver.get(cover_page_url)

counter = 7  # Antall sider som skal besøkes.
while counter > 0:
    temp_links = []

    # Finner alle interne links.
    links = driver.find_elements_by_xpath('//a[@class="crossref"]')

    # For hver link: hent link, og hvor linken peker på. Dette legges i en liste og appendes til temp_links.
    for link___ in links:
        link = link___.get_attribute('href')
        title = link___.text
        temp_links.append([link, title])

    # Finner url til siden en er på.
    url = driver.current_url

    # Finner overskriften til siden.
    title = driver.find_element_by_class_name('page-title__heading-text').text

    # Hvis du har en mappe som heter "screenshots" så blir det gjort et skjermbilde av body-en til nettsiden.
    if path.exists('screenshots'):
        pathhh = "screenshots/{}.png".format(title)
        body = driver.find_element_by_css_selector('body')
        body.screenshot(pathhh)

    # Finner en random link fra alle som er hentet ut fra siden, se linje 33.
    random_link = temp_links[random.randint(0, len(temp_links)-1)]

    # Printer hvilken side en er på og hva som er neste. Bruker randomlink identifier til dette.
    print("Har besøkt:", title, ", neste er", random_link[1])

    # Besøker den nye, tilfeldige, siden.
    driver.get(random_link[0])

    # Inkrementerer, for at løkken ikke skal være evig.
    counter -= 1

# Lukker nettleseren når programmet er ferdig.
driver.quit()
