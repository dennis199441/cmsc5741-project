import sys
from random import random

clusters = int(sys.argv[1]) # number of cluster
dimensions = int(sys.argv[2]) # number of dimensions

with open("centroids.txt", "w") as f:
	for i in range(clusters):
		for d in range(dimensions - 1):
			f.write(str(random()) + ", ")
		f.write(str(random()) + "\n")

print("Generated centroids.txt")
