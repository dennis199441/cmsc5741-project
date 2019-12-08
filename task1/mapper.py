import sys
from utils import tf, read_data
'''
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
'''
dataset = read_data("../test_data/")
for record in dataset:
	example = tf.train.Example()
	example.ParseFromString(record.numpy())
	vid = example.features.feature['id'].bytes_list.value[0].decode("utf-8")
	categories = example.features.feature['labels'].int64_list.value
	for category in categories:
		print('%s\t%s' % (category, 1))
