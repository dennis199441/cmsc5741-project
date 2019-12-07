import tensorflow as tf
import os

def read_data(folder):
	filenames = os.listdir(folder)
	if not folder.endswith("/"):
		folder = folder + "/"
	filenames = [folder + filename for filename in filenames if filename.endswith(".tfrecord")]
	dataset = tf.data.TFRecordDataset(filenames)
	return dataset

if __name__ == "__main__":
    '''
    Example of reading data and accessing feature value
    '''
    dataset = read_data("../../../Desktop/test_data/") # folder contains data
    i = 0
    for record in dataset:
        if i >= 10:
            break
        example = tf.train.Example()
        example.ParseFromString(record.numpy())
        for value in example.features.feature['id'].bytes_list.value:
            '''
            Need to refer to the protocol buffer definition
            ...bytes_list/int64_list/float_list
            '''
            print(value.decode("utf-8"))
        i += 1
