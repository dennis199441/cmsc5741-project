import sys, re, math
from random import uniform

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
	centroids = []

	with open(filepath) as fp:
		line = fp.readline()
		while line:
			if line:
				try:
					line = line.strip()
					cord = re.findall(r"[\'A-Za-z0-9.0-9a-z-0-9]+", line)
					centroids.append([float(c) for c in cord])
				except:
					break
			else:
				break
			line = fp.readline()

	fp.close()
	return centroids

def euclidean_dist(arr1, arr2):
	summ = 0
	for i in range(len(arr1)):
		summ += (arr1[i] - arr2[i])**2
	return math.sqrt(summ)

def calculateDistance(centroids):
	count_map = {}
	distance_map = {}
	for line in sys.stdin:
		if uniform(0,1) >= 0.1:
			continue
		line = line.strip()
		cord = re.findall(r"[\'A-Za-z0-9.0-9a-z-0-9]+", line)
		min_dist = math.inf
		index = -1
		try:
			cord = [float(c) for c in cord]
		except ValueError:
			continue

		for idx, centroid in enumerate(centroids):
			cur_dist = euclidean_dist(cord, centroid)
			if cur_dist < min_dist:
				min_dist = cur_dist
				index = idx

		var = "%s\t%s" % (index, min_dist)
		print(var)

if __name__ == "__main__":
	centroids = getCentroids('centroids.txt')
	calculateDistance(centroids)
