import argparse
import itertools

def file_content(filename):
    f = open(filename)
    try:
        return f.read()
    finally:
        f.close()

def prune_items(freq_items, threshold):
	prune_set = set()
	for key, value in freq_items.items():
		if value < threshold:
			prune_set.add(key)
	for key in prune_set:
		del freq_items[key]

def extract_items(freq_items):
	items = set()
	keys = set(freq_items.keys())
	for key in keys:
		items = items.union(set(key))
	return items

def apriori(baskets, threshold):
	freq_items = {}
	result = {}  # key=k , value=frequent item set
	k = 1
	for basket in baskets:
		items = basket.split(" ")
		for item in items:
			if item in freq_items:
				freq_items[item] += 1
			else:
				freq_items[item] = 1
	
	prune_items(freq_items, threshold)
	result[k] = freq_items
	apriori_helper(result, baskets, freq_items, threshold, k + 1)

	return result

def apriori_helper(result, baskets, freq_items, threshold, k):
	items = extract_items(freq_items)
	if len(items) == 0:
		return
	k_freq_items = {}
	combinations = set(itertools.combinations(items, k))
	
	for basket in baskets:
		for combination in combinations:
			if set(combination) <= set(basket.split(" ")):
				if combination in k_freq_items:
					k_freq_items[combination] += 1
				else:
					k_freq_items[combination] = 1
	prune_items(k_freq_items, threshold)
	result[k] = k_freq_items
	apriori_helper(result, baskets, k_freq_items, threshold, k + 1)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--data", dest="data", default="", help="data file", required=True)
	parser.add_argument("-s", "--threshold", dest="threshold", type=int, default=100, help="threshold")

	args = parser.parse_args()
	threshold = args.threshold
	file = args.data

	baskets = file_content(file).split("\n")
	result = apriori(baskets, threshold)
	
	i = 1
	while result[i]:
		print(i)
		print(result[i])
		i += 1