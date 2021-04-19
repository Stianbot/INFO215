import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
dc = nx.degree_centrality(G)
ev = nx.eigenvector_centrality(G)
pr = nx.pagerank(G)

color_scale = {
    1.0: "#DEEDCF",
    0.9: "#BFE1B0",
    0.8: "#99D492",
    0.7: "#74C67A",
    0.6: "#56B870",
    0.5: "#39A96B",
    0.4: "#1D9A6C",
    0.3: "#188977",
    0.2: "#137177",
    0.1: "#0E4D64",
    0.0: "#0A2F51",
}

size_scale = {
    1.0: 1100,
    0.9: 1000,
    0.8: 900,
    0.7: 800,
    0.6: 700,
    0.5: 600,
    0.4: 500,
    0.3: 400,
    0.2: 300,
    0.1: 200,
    0.0: 100,
}


def manipulate(factor, scale):
    mlist = []
    for i in factor:
        factor[i] = round(factor[i], 1)
        mlist.append(scale[factor[i]])
    return mlist



plt.title = "Degree centrality"
nx.draw(G, with_labels=True, node_color=manipulate(dc, color_scale), node_size = manipulate(dc, size_scale))
print(dc)
plt.show()

plt.title = "Eigenvector"
nx.draw(G, with_labels=True, node_color=manipulate(ev, color_scale), node_size = manipulate(ev, size_scale))
print(ev)
plt.show()

plt.title = "Page Rank"
nx.draw(G, with_labels=True, node_color=manipulate(pr, color_scale), node_size = manipulate(pr, size_scale))
print(pr)
plt.show()
