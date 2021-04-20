import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import community

G = nx.karate_club_graph()
layout = nx.spring_layout(G)

set3 = cm.get_cmap("Set3")
partition = community.best_partition(G)

nx.draw_networkx_edges(G, layout)
nx.draw_networkx_labels(G, layout)
nx.draw_networkx_nodes(G, layout, cmap=set3, node_color=list(partition.values()),
                       node_size=400)

plt.show()


t = nx.algorithms.community.label_propagation_communities(G)
t2 = nx.algorithms.community.modularity(G, t)
print(t2)
