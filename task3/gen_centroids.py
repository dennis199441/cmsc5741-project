import sys
from random import uniform

clusters = int(sys.argv[1]) # number of cluster
dimensions = int(sys.argv[2]) # number of dimensions
bound = int(sys.argv[3]) # random number bound

with open("centroids.txt", "w") as f:
	for i in range(clusters):
		for d in range(dimensions - 1):
			f.write(str(uniform(-bound, bound)) + ", ")
		f.write(str(uniform(-bound, bound)) + "\n")

print("Generated centroids.txt")
