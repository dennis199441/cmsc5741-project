from utils import tf, read_data
import sys

path = sys.argv[1]

dataset = read_data(path)
i = 0
with open('category.txt', 'w') as f:
	for record in dataset.take(6134598):
		example = tf.train.Example()
		example.ParseFromString(record.numpy())
		categories = str(example.features.feature['labels'].int64_list.value).replace("[", "").replace("]", "").replace(", ", " ") + "\n"
		f.write(categories)
		i += 1
		if i % 1000000 == 0 or i == 6134597:
			print("processed: ", i)
			
print("Preprocess completed.")