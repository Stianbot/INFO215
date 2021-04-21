import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

read_data = pd.read_csv('nutrients.csv')  # Leser inn data fra .csv
list_of_edges = np.array(read_data)  # Lager pandas dataframen om til en liste med edges.

G = nx.Graph()
G.add_edges_from(list_of_edges)  # Legger til edges i grafen (noder + labels genereres automatisk ut ifra dette)
nx.draw(G)  # Tegner nettverket
plt.show()  # Viser nettverket


