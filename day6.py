text = open('inputtxt/day6input.txt').read().splitlines()
import networkx as nx

graph = nx.DiGraph()

for line in text:
    graph.add_edge(*[x.strip() for x in line.split(')')])

print(nx.transitive_closure(graph).size())
print(nx.shortest_path_length(graph.to_undirected(), 'YOU', 'SAN') - 2)