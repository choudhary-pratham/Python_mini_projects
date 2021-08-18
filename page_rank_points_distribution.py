import networkx as nx
import matplotlib.pyplot as plt
import random


def add_edges():
    nodes = list(G.nodes())
    for s in range(len(nodes)):
        for t in range(len(nodes)):
            if(s != t):
                p = random.random()
                if(p <= 0.5):
                    G.add_edge(s, t)
    return G


def Assign_points(G):
    nodes = list(G.nodes())
    p = []
    for i in range(len(nodes)):
        p.append(100)
    return p

def distribute_points(points,G):
    nodes = list(G.nodes())
    new_points = []
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out = list(G.out_edges(n))
        if(len(out)==0):
            new_points[n] = new_points[n] + points[n]
        else:
            share = points[n]/len(out)
            for (s,t) in out:
                new_points[t] += share
    return new_points

def keep_distributing_points(points, G):
    while(1):
        new_points = distribute_points(points, G)
        print(new_points)
        points = new_points
        will = input("press q to quit and any key to continue: ")
        if(will == "q"):
            break
    return new_points

def rank_by_points(points):
    d = {}

    for i in range(len(points)):
        d[i] = points[i]
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    print(sorted_d)
    

G = nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G = add_edges()
nx.draw(G, with_labels=True)
plt.show()
# print(G.edges())
points = Assign_points(G)

final_points = keep_distributing_points(points, G)
rank_by_points(final_points)
p = nx.pagerank(G)
sorted_p = sorted(p.items(), key=lambda x: x[1])
print(sorted_p)