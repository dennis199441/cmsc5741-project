from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)

with open('audio.txt', 'w') as f:
	for record in dataset:
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		mean_audio = str(example.features.feature['mean_audio'].float_list.value).replace("[", "").replace("]", "").replace(", ", " ") + "\n"
		f.write(mean_audio)
