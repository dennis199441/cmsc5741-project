from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)
i = 0
with open('rgb.txt', 'w') as f:
	for record in dataset.take(6134598):
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		mean_rgb = str(example.features.feature['mean_rgb'].float_list.value).replace("[", "").replace("]", "").replace(", ", " ") + "\n"
		f.write(mean_rgb)
		i += 1
		if i % 1000000 == 0 or i == 6134597:
			print("processed: ", i)
			
print("Preprocess completed.")