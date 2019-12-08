from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)

with open('category.txt', 'w') as f:
	for record in dataset:
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		categories = str(example.features.feature['labels'].int64_list.value).replace("[", "").replace("]", "").replace(", ", " ") + "\n"
		f.write(categories)
