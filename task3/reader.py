from mapper import getCentroids

#check if distance of centroids and centroids1 is less than 1
def checkCentroidsDistance(centroids, centroids1):
    print(_check(centroids, centroids1))

def _check(centroids, centroids1):
    n = min(len(centroids), len(centroids1))
    i = 0
    while i < n:
        for j in range(len(centroids[i])):
            if abs(centroids[i][j] - centroids1[i][j]) >= 1:
                return 0
        i += 1
    return 1

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)