import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://no.wikipedia.org/wiki/Norges_kommuner"
request = urlopen(url)
website = BeautifulSoup(request, "html.parser")

all_data = []

for kommune in website.find_all("a", string="Vestland"):

    templist = []
    row = kommune.find_parent('tr')

    if row is not None:
        for cell in row.find_all('td'):
            instance = cell.get_text().rstrip('\n').replace("\xa0", "")
            if instance != "":
                templist.append(instance)

    all_data.append(templist)


nodes = []
edges = []
attributes = []


for k in all_data:
    print(k)
    nodes.append(k[1])
    edges.append((k[1], k[3]))
    attributes.append([int(k[4]), k[6]])

G = nx.Graph()

G.add_nodes_from(nodes)


counter = 0
for n in nodes:
    G.nodes[n]['language'] = attributes[counter][1]
    G.nodes[n]['population'] = attributes[counter][0]
    counter += 1

color_map = []
language = nx.get_node_attributes(G, 'language')

for no in language:
    if language[no].lower() == "bokmål":
        color_map.append("pink")
    elif language[no].lower() == "nynorsk":
        color_map.append("yellow")
    else:
        color_map.append("grey")


size_map = []
for s in G.nodes:
    size = G.nodes[s]["population"]
    size_map.append(round(float(size)/10))

color_map.append("blue")
size_map.append(300)

G.add_node("Vestland")


G.add_edges_from(edges)
pos = nx.spring_layout(G)



plt.figure(figsize=(15, 15))

nx.draw_networkx(G, pos, node_color=color_map, node_size=size_map, font_size=22)

# Lagrer grafen
plt.savefig("Vestland.png", format="PNG", dpi=300)
plt.show()
