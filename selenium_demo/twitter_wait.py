from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Eksempel på hvordan en kan få driveren til å vente til elementer av nettsiden er lastet.
'''

url = 'https://twitter.com/search?q=%23Bergen'
driver = webdriver.Firefox()
driver.get(url)


# Funksjon for å vente til "partial_link_text" finnes på nettsiden. Det den venter på er en hashtag (#).
def wait_until():
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.PARTIAL_LINK_TEXT, "#")))


wait_until()

driver.quit()
