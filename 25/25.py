from collections import defaultdict
from matplotlib import pyplot as plt


lines = [x.strip() for x in open("25")]




nodes = defaultdict(lambda: [])

for l in lines:
    p = l.split(": ")
    for pp in p[1].split(" "):
        nodes[p[0]].append(pp)
        nodes[pp].append(p[0])



def del_con(n1, n2):
    nodes[n1].remove(n2)
    nodes[n2].remove(n1)


del_con('zlv', 'bmx')
del_con('lrd', 'qpg')
del_con('tpb', 'xsl')


import networkx as nx

G = nx.Graph()

for intersection in nodes:
    G.add_node(intersection)

for intersection in nodes:
    for next in nodes[intersection]:
        G.add_edge(intersection, next)

sub_graphs = (G.subgraph(c) for c in nx.connected_components(G))

for i, sg in enumerate(sub_graphs):
    print ("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
    # print ("\tNodes:", sg.nodes(data=True))
    # print ("\tEdges:", sg.edges())

# nx.draw(G, with_labels=True, font_weight='bold')

# plt.show()