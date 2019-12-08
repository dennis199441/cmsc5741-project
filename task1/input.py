import sys
from utils import tf, read_data

data_path = sys.argv[1]
dataset = read_data(data_path)
with open('test_data.txt', "wb") as f:
	for record in dataset:
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		vid = example.features.feature['id'].bytes_list.value[0].decode("utf-8")
		categories = example.features.feature['labels'].int64_list.value
		f.write(str(categories).replace("[", "").replace("]","").replace(", ", "\t"))