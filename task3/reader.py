from mapper import getCentroids

#check if distance of centroids and centroids1 is less than 1
def checkCentroidsDistance(centroids, centroids1):
    n = min(len(centroids), len(centroids1))
    i, flag = 0, 1
    while i < n:
        for j in range(2):
            if abs(centroids[i][j] - centroids1[i][j]) < 1:
                flag = 0
                break

    print(flag)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)
