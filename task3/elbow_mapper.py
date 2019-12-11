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
					centroids.append([float(cord[0]), float(cord[1])])
				except:
					break
			else:
				break
			line = fp.readline()

	fp.close()
	return centroids

def calculateDistance(centroids):
	count_map = {}
	distance_map = {}
	for line in sys.stdin:
		line = line.strip()
		cord = re.findall(r"[\'A-Za-z0-9.0-9]+", line)
		min_dist = 10000000000000
		target_cluster = 0
		for k in range(len(centroids)):
			dist, summ = 0, 0
			for i in range(len(cord)):
				summ += pow(float(cord[i]) - centroids[k][i], 2)
			dist += sqrt(summ)
			if dist < min_dist:
				min_dist = dist
				target_cluster = k
		var = "%s\t%s\t%s" % (target_cluster, min_dist, 1)
		print(var)

if __name__ == "__main__":
	centroids = getCentroids('centroids.txt')
	calculateDistance(centroids)
