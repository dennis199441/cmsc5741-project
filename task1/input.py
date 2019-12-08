import sys
from utils import tf, read_data

data_path = sys.argv[1]
dataset = read_data(data_path)
for record in dataset:
	example = tf.train.Example()
	example.ParseFromString(record.numpy())
	vid = example.features.feature['id'].bytes_list.value[0].decode("utf-8")
	categories = example.features.feature['labels'].int64_list.value
	print('#', str(categories).replace("[", "").replace("]","").replace(", ", "\t"))