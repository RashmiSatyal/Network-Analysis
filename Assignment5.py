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





