#!/bin/bash
hadoop fs -rm -r /yt8m-analysis/task3

hadoop fs -put . /yt8m-analysis/task3

if [ ! -d "./elbow_result" ]
then
	mkdir ./elbow_result
else
	rm ./elbow_result/*
fi

k=1
while :
do
	rm centroids*.txt

	python3 gen_centroids.py $k 2 10

	i=1
	while :
	do
		yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
		-files hdfs:///yt8m-analysis/task3/centroids.txt,hdfs:///yt8m-analysis/task3/mapper.py,hdfs:///yt8m-analysis/task3/reducer.py \
		-mapper 'python3 mapper.py' \
		-reducer 'python3 reducer.py' \
		-input /yt8m-analysis/task3/test_dataset.txt \
		-output /yt8m-analysis/task3/output$i

		rm -f centroids1.txt
		hadoop fs -copyToLocal /yt8m-analysis/task3/output$i/part-00000 centroids1.txt
		seeiftrue=`python3 reader.py 1`
		if [ $seeiftrue = 1 ]
		then
			rm centroids.txt
			hadoop fs -copyToLocal /yt8m-analysis/task3/output$i/part-00000 centroids.txt
			break
		else
			rm centroids.txt
			hadoop fs -copyToLocal /yt8m-analysis/task3/output$i/part-00000 centroids.txt
		fi
		i=$((i+1))
	done

	yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
	-files hdfs:///yt8m-analysis/task3/centroids.txt,hdfs:///yt8m-analysis/task3/elbow_mapper.py,hdfs:///yt8m-analysis/task3/elbow_reducer.py \
	-mapper 'python3 elbow_mapper.py' \
	-reducer 'python3 elbow_reducer.py' \
	-input /yt8m-analysis/task3/test_dataset.txt \
	-output /yt8m-analysis/task3/elbow_output$k

	hadoop fs -copyToLocal /yt8m-analysis/task3/elbow_output$k/part-00000 elbow$k.txt
	
	k=$((k+1))
done