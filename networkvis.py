import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
df = pd.read_csv('new_lsa.out', sep='\t')

all_weights = []
all_nodes = []
for i in range(len(df['X'])):
    if(np.abs(df['LS'][i]) < 0.3):
        continue

    G.add_edge(df['X'][i], df['Y'][i], weight=df['LS'][i])
    all_weights.append(df['LS'][i])
    all_nodes.append(df['X'][i])
    all_nodes.append(df['Y'][i])

unique_weights = list(set(all_weights))
unique_nodes = list(set(all_nodes))

pos = nx.spring_layout(G, k=20)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if np.abs(d['weight']) > 0.5 and d['weight'] > 0]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if np.abs(d['weight']) <= 0.5 and d['weight'] > 0]

nelarge = [(u, v) for (u, v, d) in G.edges(data=True) if np.abs(d['weight']) > 0.5 and d['weight'] < 0]
nesmall = [(u, v) for (u, v, d) in G.edges(data=True) if np.abs(d['weight']) <= 0.5 and d['weight'] < 0]

nx.draw_networkx_edges(G, pos, edgelist=elarge, width=4, edge_color='b')
nx.draw_networkx_edges(G, pos, edgelist=esmall, alpha=0.5, edge_color='b', style='dashed', width=2)

nx.draw_networkx_edges(G, pos, edgelist=nelarge, width=4, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=nesmall, alpha=0.5, edge_color='r', style='dashed', width=2)

nx.draw_networkx_nodes(G, pos, node_size=7000, node_color='lightgray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.axis('off')
plt.show()
