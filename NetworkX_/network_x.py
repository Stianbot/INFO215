import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

kommuner = ["Bergen", "Askøy", "Øygarden"]
grenser = [("Bergen", "Askøy"), ("Bergen", "Øygarden"), ("Askøy", "Øygarden")]

G.add_nodes_from(kommuner)
G.add_edges_from(grenser)

G.add_node("Vaksdal")
G.add_edge("Vaksdal", "Bergen")

print(G.nodes, G.edges)

layout = nx.spring_layout(G)
color_list = ["pink", "yellow", "green", "blue"]
size_list = [1000, 250, 300, 100]

nx.draw_networkx_nodes(G, layout, node_color=color_list, node_size=size_list)
nx.draw_networkx_edges(G, layout)
nx.draw_networkx_labels(G, layout)

plt.show()
