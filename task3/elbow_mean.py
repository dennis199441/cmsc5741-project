import os, sys

path = sys.argv[1] # elbow results
k = int(sys.argv[2]) # k value
result = []
summ = 0
i = 1
while i <= k:
	print("i = {}".format(i))
	with open(path + "{}_elbow.txt".format(i), "r") as f:
		line = f.readline()
		count = 0
		while line:
			if line:
				count += 1
				try:
					line = line.strip()
					line = line.split()
					summ += float(line[1])
					print(line)
				except:
					break
			line = f.readline()
	f.close()
	result.append(summ/count)
	summ = 0
	i += 1

print(result)
