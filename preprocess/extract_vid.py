from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)
i = 0
with open('vid.txt', 'w') as f:
	for record in dataset.take(6134598):
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		vid = example.features.feature['id'].bytes_list.value[0].decode("utf-8") + "\n"
		f.write(vid)
		i += 1
		if i % 1000000 == 0 or i == 6134597:
			print("processed: ", i)
			
print("Preprocess completed.")