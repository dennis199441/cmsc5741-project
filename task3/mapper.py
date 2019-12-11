import sys, re
import math

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
	centroids = []

	with open(filepath) as fp:
		line = fp.readline()
		while line:
			if line:
				try:
					line = line.strip()
					cord = re.findall(r"[\'A-Za-z0-9.0-9a-z0-9]+", line)
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

# create clusters based on initial centroids
def createClusters(centroids):
	for line in sys.stdin:
		line = line.strip()
		cord = re.findall(r"[\'A-Za-z0-9.0-9a-z0-9]+", line)
		min_dist = math.inf
		index = -1

		for idx, centroid in enumerate(centroids):
			try:
				cord = [float(c) for c in cord]
			except ValueError:
				continue

			# euclidian distance from every point of dataset
			# to every centroid
			cur_dist = euclidean_dist(cord, centroid)

			# find the centroid which is closer to the point
			if cur_dist < min_dist:
				min_dist = cur_dist
				index = idx

		var = str(index) + "\t"
		for i in range(len(cord) - 1):
			append = str(cord[i]) + "\t"
			var += append
		var += str(cord[-1])
		print(var)

if __name__ == "__main__":
	centroids = getCentroids('centroids.txt')
	createClusters(centroids)
