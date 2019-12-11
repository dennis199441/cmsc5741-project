import sys

dist_map = {}
cnt_map = {}
current_cluster = None
current_dist = 0
current_count = 0
cluster = None

for line in sys.stdin:
	line = line.strip()
	
	cluster, dist = line.split('\t')
	try:
		dist = float(dist)
	except ValueError:
		continue
		
	if current_cluster == cluster:
		current_dist += dist
		current_count += 1
	else:
		if current_cluster:
			print("%s\t%s" % (current_cluster, current_dist/current_count))
		current_dist = dist
		current_count = 1
		current_cluster = cluster

if current_cluster == cluster:
	print("%s\t%s" % (current_cluster, current_dist/current_count))