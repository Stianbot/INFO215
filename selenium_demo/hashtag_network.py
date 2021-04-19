from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import networkx as nx
import matplotlib.pyplot as plt
import time


# Program for creating a twitter hashtag network. Does not go in depth, only creates an ego network
# for one particular hashtag.


def scrolldown():
    for i in range(30):
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(.3)


nodes = []
edges = []

driver = webdriver.Firefox()


def find_hashtag(hashtag):
    url = f'https://twitter.com/hashtag/{hashtag}?src=hashtag_click'
    driver.get(url)

    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.PARTIAL_LINK_TEXT, "#")))

    scrolldown()

    a = driver.find_elements_by_tag_name('a')
    blacklist = f"(?!{hashtag.lower()})(?!{hashtag.upper()})(?!{hashtag.capitalize()})"
    full = f"(https:\/\/twitter\.com\/hashtag\/){blacklist}.*=hashtag_click"
    regex = re.compile(full)

    for link in a:
        url = link.get_attribute('href')
        hashtag_text = link.get_attribute('text')
        if regex.match(url) is not None:
            nodes.append(hashtag_text)
            edges.append((f"#{hashtag}", hashtag_text))


find_hashtag("Trondheim")
find_hashtag("Stavanger")

print(nodes, edges)

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
nx.draw(G, with_labels=True)
name = "Trondheim_Stavanger_network"
nx.write_graphml(G, f"{name}.graphml")
plt.show()

driver.quit()

