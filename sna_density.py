from numpy import genfromtxt
import numpy as np
import networkx as nx
import os


fileName = "2020_NetworkExercise_1st_Matrix.csv"
mydata = genfromtxt(fileName, delimiter=';')

adjacency = mydata[1:,1:]
print(adjacency)

rows, cols = np.where(adjacency == 1)
edges = zip(rows.tolist(), cols.tolist())
gr = nx.Graph(adjacency)
gr.add_edges_from(edges)
print(f"Density: {nx.density(gr)}")

