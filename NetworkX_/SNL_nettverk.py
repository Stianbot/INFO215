from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go


countries = ["https://snl.no/Norge","https://snl.no/Tyskland","https://snl.no/Russland"]

all_nodes = []
all_edges = []
visited = []
dead_links = []

def get_page(url):
    try:
        request = urlopen(url)
        webpage = BeautifulSoup(request, "html.parser")
        visited.append(url)
        return webpage
    except:
        dead_links.append(url)



n = get_page(countries[0])

def get_links(page):
    old_current = page.find(class_="page-title__heading-text").get_text()
    current = "".join(old_current.split())
    print(current)
    data = {
        "nodes": [],
        "edges": [],
        "urls": []
    }
    for link in page.find_all(attrs={"class": 'crossref'}):
        data["nodes"].append(link.get_text())
        data["urls"].append(link.attrs["href"])
        data["edges"].append((current, link.get_text()))

        all_nodes.append(link.get_text())
        all_edges.append((current, link.get_text()))

    return data

first_step = get_links(n)


def deeper(data, limit=10):

    for link in data["urls"][:limit]:
        try:
            if link != [n for n in visited]:
                more = get_links(get_page(link))
                global all_nodes
                global all_edges
                all_nodes += more["nodes"]
                all_edges += more["edges"]
        except:
            continue

deeper(first_step)

all_nodes = list(set(all_nodes))
print(all_nodes, len(all_nodes))
print(all_edges, len(all_edges))
print(dead_links)
print(visited)


G = nx.Graph()

G.add_nodes_from(all_nodes)
G.add_edges_from(all_edges)

nx.draw(G)
nx.write_graphml(G,"nettverk.graphml")
plt.show()
