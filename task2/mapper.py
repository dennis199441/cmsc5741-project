import sys, metadata, itertools

def extract_items(candidates):
	items = set()
	for candidate in candidates:
		items = items.union(set(candidate))
	return items

def prune_items(freq_items, threshold):
	prune_set = set()
	for k, v in freq_items.items():
		if v < threshold:
			prune_set.add(k)
	for k in prune_set:
		del freq_items[k]

def prepare_threshold(threshold, dest="./metadata.py"):
	with open(dest, "w") as f:
		f.write("threshold={}\n".format(threshold))
		f.write("k={}\n".format(k))

def prepare_next_candidate(candidate, dest=f"./candidates.py"):
	items = extract_items(candidate)
	combinations = set(itertools.combinations(items, k + 1))
	with open(dest, 'w') as filetowrite:
		filetowrite.write(f"k_candidate={}\n".format(k))
		filetowrite.write(f"candidate={}\n".format(candidate))
		filetowrite.write(f"combinations={}\n".format(combinations))

for line in sys.stdin:
	line = line.strip()
	items = line.split()
	if metadata.k == 1:
		for item in items:
			print("%s\t%s" % (item, 1))
	else:
		if candidates.k_candidate != metadata.k - 1:
			raise Exception("Invalid k value, Previous k = {}, current k = {}".format(k_candidate, metadata.k))
		for basket in items:
			items = set(basket.split(" "))
			for combination in candidates.combinations:
				if set(combination) <= set(items):
					print("{}\t{}".format(combination, 1))
