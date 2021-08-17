import networkx as nx
import matplotlib.pyplot as plt
import random
import operator
G = nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
# plt.show() -----> to print the random graph 
dict = {}
for i in range(G.number_of_nodes()):
    dict[i] = 0
x = random.choice([i for i in range(G.number_of_nodes())])
dict[x]+=1
for i in range(100000000):
    list_new = list(G.neighbors(x))
    if(len(list_new)==0):# if it is a sink then check for any random node
        x= random.choice([i for i in range(G.number_of_nodes())])
    else:# choosing randomly from the list of neighbors
        x = random.choice(list_new)
    dict[x]+=1
p = nx.pagerank(G)
sorted_p = sorted(p.items(),key=operator.itemgetter(1))# 1 for sort by values and sort and 0 for sort by key
sorted_dict = sorted(dict.items(),key=operator.itemgetter(1)) # 1 for sort by values and sort and 0 for sort by key
print(sorted_dict)
print(sorted_p)
