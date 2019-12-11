import sys, re
from math import sqrt

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
	centroids = []

	with open(filepath) as fp:
		line = fp.readline()
		while line:
			if line:
				try:
					line = line.strip()
					cord = re.findall(r"[\'A-Za-z0-9.0-9]+", line)
					centroids.append([float(c) for c in cord])
				except:
					break
			else:
				break
			line = fp.readline()

	fp.close()
	return centroids

# create clusters based on initial centroids
def createClusters(centroids):
	for line in sys.stdin:
		line = line.strip()
		cord = re.findall(r"[\'A-Za-z0-9.0-9]+", line)
		min_dist = 100000000000000
		index = -1

		for centroid in centroids:
			try:
				cord = [float(c) for c in cord]
			except ValueError:
				continue

			# euclidian distance from every point of dataset
			# to every centroid
			for i in range(len(cord)):
				summ += pow(cord[i] - centroid[i], 2)
			cur_dist = sqrt(summ)

			# find the centroid which is closer to the point
			if cur_dist <= min_dist:
				min_dist = cur_dist
				index = centroids.index(centroid)

		var = str(index) + "\t"
		for i in range(len(cord)) - 1:
			append = str(cord[i]) + "\t"
			var += append
		var += str(cord[-1])
		print(var)

if __name__ == "__main__":
	centroids = getCentroids('centroids.txt')
	createClusters(centroids)
