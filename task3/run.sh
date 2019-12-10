#!/bin/bash
i=1
while :
do
	yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
	-files hdfs:///yt8m-analysis/task3/centroids.txt,hdfs:///yt8m-analysis/task3/mapper.py,hdfs:///yt8m-analysis/task3/reducer.py \
	-mapper 'python3 mapper.py' \
	-reducer 'python3 reducer.py 10' \
	-input /yt8m-analysis/task3/test_dataset.txt \
	-output /yt8m-analysis/task3/output$i

	rm -f centroids1.txt
	hadoop fs -copyToLocal /yt8m-analysis/task3/output$i/part-00000 centroids1.txt
	seeiftrue=`python3 reader.py`
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
