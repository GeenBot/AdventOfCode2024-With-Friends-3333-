import networkx as nx
import sys

def build(cons):
    graph = nx.Graph()
    for a, b in cons:
        graph.add_edge(a, b)
    return graph

def find_ts(graph):
    ts = []
    for t in nx.enumerate_all_cliques(graph):
        if len(t) == 3:
            ts.append(tuple(sorted(t)))
    return ts

def s1(cons):
    graph = build(cons)
    ts = find_ts(graph)
    return sum(1 for t in ts if any(node.startswith('t') for node in t))

def s2(cons):
    graph = build(cons)
    clique = max(list(nx.find_cliques(graph)), key=len)
    return ','.join(sorted(clique))

with open(sys.argv[1]) as f:
    cons = [line.strip().split('-') for line in f.read().strip().split('\n')]
    print(s1(cons))
    print(s2(cons))
