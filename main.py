
import igraph as ig
from igraph import Graph
import networkx as nx
import sys

if __name__ == "__main__":
    var = sys.argv[1]
    G = nx.read_adjlist(var, nodetype=int)
    print("min_edge_cover:")
    print(nx.min_edge_cover(G))
    print(len(nx.min_edge_cover(G)))
