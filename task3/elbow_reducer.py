import sys

dist_map = {}
cnt_map = {}
current_cluster = None
current_dist = 0
current_count = 0
cluster = None

for line in sys.stdin:
	line = line.strip()
	print(line)
	'''
	cluster, dist, count = line.split('\t')
	try:
		dist = float(dist)
		count = float(count)
	except ValueError:
		continue
		
	if current_cluster == cluster:
		current_dist += dist
		current_count += count
	else:
		if current_cluster:
			if current_cluster not in dist_map:
				dist_map[current_cluster] = current_dist
			else:
				dist_map[current_cluster] += current_dist
			if current_cluster not in cnt_map:
				cnt_map[current_cluster] = current_count
			else:
				cnt_map[current_cluster] += current_count
		current_dist = dist
		current_count = count
		current_cluster = cluster

if current_cluster == cluster:
	if current_cluster not in dist_map:
		dist_map[current_cluster] = current_dist
	else:
		dist_map[current_cluster] += current_dist
	if current_cluster not in cnt_map:
		cnt_map[current_cluster] = current_count
	else:
		cnt_map[current_cluster] += current_count

sum_dist = 0
n = len(dist_map)
for i in range(n):
	sum_dist += (dist_map[i] / cnt_map[i])
avg_dist = sum_dist / n
print("%s" % str(avg_dist))
'''