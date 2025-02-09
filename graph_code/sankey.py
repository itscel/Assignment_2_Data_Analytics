import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio 
import os

if not os.path.exists('images'):
    os.makedirs('images')  



df = pd.read_csv('csv/sankey_assignment.csv')

from_nodes = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
to_nodes = ['Reg', 'Aca', 'Oth']

node_labels = from_nodes + to_nodes

def get_node_index(node, nodes_list):
    return nodes_list.index(node)

sources = []
targets = []
values = []

for index, row in df.iterrows():
    for i, from_node in enumerate(from_nodes):
        for j, to_node in enumerate(to_nodes):
            flow_value = row[from_node] * row[to_node]
            if flow_value > 0:
                sources.append(get_node_index(from_node, node_labels))
                targets.append(get_node_index(to_node, node_labels))
                values.append(flow_value)

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
))

fig.update_layout(title_text="Sankey Diagram", font_size=10)

pio.write_image(fig, 'images/sankey.png', scale=3)  

fig.show()
