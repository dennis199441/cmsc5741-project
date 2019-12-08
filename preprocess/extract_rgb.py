from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)

with open('rgb.txt', 'w') as f:
	for record in dataset:
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		mean_rgb = str(example.features.feature['mean_rgb'].float_list.value).replace("[", "").replace("]", "").replace(", ", " ") + "\n"
		f.write(mean_rgb)
