import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv('csv/networks_assignment.csv')

center_nodes = ['D', 'F', 'I', 'N', 'S']
green_nodes = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA']
yellow_nodes = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']

G = nx.Graph()

# Add nodes to the graph with colors
node_colors = {}
for node in center_nodes:
    G.add_node(node, color='blue')
    node_colors[node] = 'blue'

for node in green_nodes:
    G.add_node(node, color='green')
    node_colors[node] = 'green'

for node in yellow_nodes:
    G.add_node(node, color='yellow')
    node_colors[node] = 'yellow'

for index, row in df.iterrows():
    label = row['LABELS']
    for column in df.columns[1:]: 
        if row[column] > 0:
            G.add_edge(label, column, weight=row[column])

pos = {}
angle_step = 360 / len(center_nodes)
for i, node in enumerate(center_nodes):
    angle = i * angle_step
    pos[node] = (3 * np.cos(np.radians(angle)), 3 * np.sin(np.radians(angle)))

outside_nodes = list(set(G.nodes) - set(center_nodes))
for i, node in enumerate(outside_nodes):
    pos[node] = (6 * np.cos(np.radians(i * 360 / len(outside_nodes))), 
                 6 * np.sin(np.radians(i * 360 / len(outside_nodes))))

for node in G.nodes():
    if node not in node_colors:
        node_colors[node] = 'gray'

plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color=[node_colors[node] for node in G.nodes()],
        node_size=500, font_size=10, font_weight='bold', edge_color='gray', width=1.5)
plt.title("Network Graph")

plt.savefig('images/network.png', dpi=300, bbox_inches='tight') 


plt.show()
