import sys

def elementSum(arr1, arr2):
    n = len(arr1)
    ret = []
    for i in range(n):
        v = arr1[i] + arr2[i]
        ret.append(v)
    return ret

def printSumm(summ, count):
    val = ""
    for i in range(len(summ)-1):
        v = str(summ[i] / count) + ", "
        val += v
    val += str(summ[-1] / count)
    print(val)

def calculateNewCentroids():
    current_centroid = None
    summ = []
    # sum_x = 0
    # sum_y = 0
    count = 0

    # input comes from STDIN
    for line in sys.stdin:

        # parse the input of mapper.py
        # centroid_index, x, y = line.split('\t')
        line = line.strip()
        data = line.split("\t")
        centroid_index = data[0]
        # convert coord (currently a string) to float
        coord = [float(data[i]) for i in range(1, len(data))]
        
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_centroid == centroid_index:
            count += 1
            summ = elementSum(summ, coord)
        else:
            if count != 0:
                # print the average of every cluster to get new centroids
                # print(str(sum_x / count) + ", " + str(sum_y / count))
                printSumm(summ, count)

            current_centroid = centroid_index
            summ = coord
            count = 1
    
    # print last cluster's centroids
    if current_centroid == centroid_index and count != 0:
        printSumm(summ, count)
        # print(str(sum_x / count) + ", " + str(sum_y / count))

def test_reducer():
    for line in sys.stdin:
        line = line.strip()
        print(line)

if __name__ == "__main__":
    calculateNewCentroids()
    # test_reducer()
