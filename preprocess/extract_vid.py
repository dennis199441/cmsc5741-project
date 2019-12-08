from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)

with open('vid.txt', 'w') as f:
	for record in dataset:
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		vid = example.features.feature['id'].bytes_list.value[0].decode("utf-8") + "\n"
		f.write(vid)
