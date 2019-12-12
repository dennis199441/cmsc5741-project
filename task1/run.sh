hadoop fs -rm -r /yt8m-analysis/task1/

hadoop fs -put . /yt8m-analysis/task1

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task1/mapper.py,hdfs:///yt8m-analysis/task1/reducer.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer.py' \
-input /preprocessed_data/category.txt \
-output /yt8m-analysis/task1/output

hadoop fs -text /yt8m-analysis/task1/output/*
