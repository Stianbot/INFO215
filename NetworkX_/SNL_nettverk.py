from urllib.request import urlopen
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

# Lister med lenker fra snl.no som skal være utgangspunkt for nettverket.
countries = ["https://snl.no/Norge", "https://snl.no/Sverige", "https://snl.no/Danmark"]
parties = ["https://snl.no/Arbeiderpartiet", "https://snl.no/Senterpartiet", "https://snl.no/H%C3%B8yre",]

all_nodes = []  # Global variabel for samling av alle noder.
all_edges = []  # Global variabel for samling av alle edger.
visited = []  # Global variabel over alle sidene som er besøkt.
dead_links = []  # Global variabel over alle døde lenker programmet finner.


# Funksjon som henter ned en nettside og returnerer et BeautifulSoup objekt av nettsiden.
def get_page(url):
    try:
        request = urlopen(url)
        webpage = BeautifulSoup(request, "html.parser")
        visited.append(url)
        return webpage
    except:
        dead_links.append(url)


# Funksjon som henter ut alle lenker fra et nettsideobjekt (beautifulsoup).
# Funksjonen lager også noder og edger for lenkene på siden.
def get_links(page):

    # Finner overskriften til nettsiden.
    old_current = page.find(class_="page-title__heading-text").get_text()
    current = "".join(old_current.split()) # Fjerner whitespace rundt overskriften.
    current = current.lower()
    print(f"currently on: {current}")

    data = {
        "nodes": [],
        "edges": [],
        "urls": []
    }
    for link in page.find_all(attrs={"class": 'crossref'}):
        data["nodes"].append(link.get_text().lower())
        data["urls"].append(link.attrs["href"])
        data["edges"].append((current, link.get_text().lower()))

        all_nodes.append(link.get_text().lower())
        all_edges.append((current, link.get_text().lower()))

    return data


def deeper(data, limit=2):
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

# Funksjon som scraper snl.no og lager ett nettverk. Lager en .graphml fil av nettverket.
def program(list_of_urls, name, limit):
    """
    :param list_of_urls: Liste over urls som er utgangspunktet for nettverket.
    :param name: navnet til .graphml filen som lages.
    :param limit: Antall lenker som skal besøkes videre fra utgangspunktsidene.
    """
    for i in list_of_urls:
        p = get_page(i)
        y = get_links(p)
        deeper(y, limit=limit)

    global all_nodes
    all_nodes = list(set(all_nodes))
    G = nx.Graph()
    G.add_nodes_from(all_nodes)
    G.add_edges_from(all_edges)
    nx.draw(G)

    nx.write_graphml(G, f"graphs/{name}.graphml")
    plt.show()


program(countries, "norge_danmark_sverige", 5)
