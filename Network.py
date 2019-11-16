import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/NDSU/Introduction to Data Mining/Assignments/Assignment 5/networkDatasets/karate.txt", delimiter=r"\s+",names=["col_a","col_b"])
data = pd.crosstab(data.col_a,data.col_b)

data.loc[:,'Total'] = data.sum(axis=1)

list_j = data['Total'].unique().tolist()
list_j.sort()

list_kj = data['Total'].value_counts(sort=False).tolist()
print(data['Total'].value_counts(sort=False))
sum_total = data['Total'].sum()
print(data)
print(list_j)
print(list_kj)
print(sum_total)

pj = list(range(len(list_kj)))
for index, i in enumerate(list_kj):
	pj[index] = i/sum_total

lpj = [ pow(10,i) for i in pj ]
lj = [ pow(10,i) for i in list_j ]
print(lpj)
print(lj)
plt.plot(lj,pj)
# plt.show()

print(pj)

print ("#############################################################################################")



def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G

def tup(filename):
	with open(filename) as file:
		
		mylist = [tuple(list(map(int, i.split(' ')))) for i in file]
	return mylist


net_tuples = tup("D:/NDSU/Introduction to Data Mining/Assignments/Assignment 5/networkDatasets/karate.txt")
print(net_tuples)

G ={}

for (x,y) in net_tuples: make_link(G,x,y)

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return -1.0
    links = 0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))

total = 0
for v in G.keys():
    total += clustering_coefficient(G,v)

print (total/len(G))


print (clustering_coefficient(G,2))
