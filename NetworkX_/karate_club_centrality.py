import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

G = nx.karate_club_graph()

dc = nx.degree_centrality(G)
ev = nx.eigenvector_centrality(G)
pr = nx.pagerank(G)

layout = nx.spring_layout(G)

dc_color = cm.get_cmap("viridis")
ev_color = cm.get_cmap("plasma")
pr_color = cm.get_cmap("cividis")

nx.draw_networkx_edges(G, layout)
nx.draw_networkx_labels(G, layout)
nx.draw_networkx_nodes(G, layout, cmap=dc_color, node_color=list(dc.values()),
                       node_size=list([n*800 for n in dc.values()]))

plt.show()

nx.draw_networkx_edges(G, layout)
nx.draw_networkx_nodes(G, layout, cmap=ev_color, node_color=list(ev.values()),
                       node_size=list([n*800 for n in ev.values()]))
nx.draw_networkx_labels(G, layout)
plt.show()

nx.draw_networkx_edges(G, layout)
nx.draw_networkx_nodes(G, layout, cmap=pr_color, node_color=list(pr.values()),
                       node_size=list([n*5000 for n in pr.values()]))
nx.draw_networkx_labels(G, layout)
plt.show()
