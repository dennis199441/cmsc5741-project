#!/bin/bash
hadoop fs -rm -r /yt8m-analysis/task3

hadoop fs -put . /yt8m-analysis/task3

if [ ! -d "./elbow_result" ]
then
	mkdir ./elbow_result
else
	echo "elbow_result exists!"
#	rm ./elbow_result/*
fi

if [ ! -d "./kmeans_result" ]
then
	mkdir ./kmeans_result
else
	echo "kmeans_result exists"
#	rm ./kmeans_result/*
fi

k=1
while :
do
	rm centroids*.txt

	python3 gen_centroids.py $k 2 2

	hadoop fs -put -f ./centroids.txt /yt8m-analysis/task3/centroids.txt
	
	echo "[DEBUG] START KMEANS ALGORITHM: k=${k}"
	
	i=1
	while :
	do
		yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
		-files hdfs:///yt8m-analysis/task3/centroids.txt,hdfs:///yt8m-analysis/task3/mapper.py,hdfs:///yt8m-analysis/task3/reducer.py \
		-mapper 'python3 mapper.py' \
		-reducer 'python3 reducer.py' \
		-input /preprocessed_data/audio.txt \
		-output /yt8m-analysis/task3/${k}_output$i

		rm -f centroids1.txt
		hadoop fs -copyToLocal /yt8m-analysis/task3/${k}_output$i/part-00000 centroids1.txt
		seeiftrue=`python3 reader.py 1`
		if [ $seeiftrue = 1 ]
		then
			rm centroids.txt
			hadoop fs -copyToLocal /yt8m-analysis/task3/${k}_output$i/part-00000 centroids.txt
			hadoop fs -copyToLocal /yt8m-analysis/task3/${k}_output$i/part-00000 ./kmeans_result/${k}_centroids.txt
			break
		else
			rm centroids.txt
			hadoop fs -copyToLocal /yt8m-analysis/task3/${k}_output$i/part-00000 centroids.txt
		fi
		i=$((i+1))
	done
	
	echo "[DEBUG] START ELBOW METHOD"
	
	hadoop fs -put -f ./centroids.txt /yt8m-analysis/task3/centroids.txt

	yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
	-files hdfs:///yt8m-analysis/task3/centroids.txt,hdfs:///yt8m-analysis/task3/elbow_mapper.py,hdfs:///yt8m-analysis/task3/elbow_reducer.py \
	-mapper 'python3 elbow_mapper.py' \
	-reducer 'python3 elbow_reducer.py' \
	-input /preprocessed_data/audio.txt \
	-output /yt8m-analysis/task3/elbow_output$k

	hadoop fs -copyToLocal /yt8m-analysis/task3/elbow_output$k/part-00000 ./elbow_result/${k}_elbow.txt
	
	k=$((k+1))
done
