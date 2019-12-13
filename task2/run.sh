# Implemented mapreduced based apriori algorithm and executed using different support value
# support value = 10
hadoop fs -rm -r /yt8m-analysis/task2/2itemsets_10_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/2itemsets_mapper.py,hdfs:///yt8m-analysis/task2/2itemsets_reducer.py \
-mapper 'python3 2itemsets_mapper.py' \
-reducer 'python3 2itemsets_reducer.py 10' \
-input /preprocessed_data/category.txt \
-output /yt8m-analysis/task2/2itemsets_10_output

# save result
hadoop fs -text /yt8m-analysis/task2/2itemsets_10_output/* > ./2itemsets_10.txt
hadoop fs -put ./2itemsets_10.txt /yt8m-analysis/task2/
# print sorted result
# sort 2itemsets_10.txt | uniq | sort -nr


# support value = 20
hadoop fs -rm -r /yt8m-analysis/task2/2itemsets_20_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/2itemsets_mapper.py,hdfs:///yt8m-analysis/task2/2itemsets_reducer.py \
-mapper 'python3 2itemsets_mapper.py' \
-reducer 'python3 2itemsets_reducer.py 20' \
-input /preprocessed_data/category.txt \
-output /yt8m-analysis/task2/2itemsets_20_output

# save result
hadoop fs -text /yt8m-analysis/task2/2itemsets_20_output/* > ./2itemsets_20.txt
hadoop fs -put ./2itemsets_20.txt /yt8m-analysis/task2/
# print sorted result
# sort 2itemsets_20.txt | uniq | sort -nr



# support value = 50
hadoop fs -rm -r /yt8m-analysis/task2/2itemsets_50_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/2itemsets_mapper.py,hdfs:///yt8m-analysis/task2/2itemsets_reducer.py \
-mapper 'python3 2itemsets_mapper.py' \
-reducer 'python3 2itemsets_reducer.py 50' \
-input /preprocessed_data/category.txt \
-output /yt8m-analysis/task2/2itemsets_50_output

# save result
hadoop fs -text /yt8m-analysis/task2/2itemsets_50_output/* > ./2itemsets_50.txt
hadoop fs -put ./2itemsets_50.txt /yt8m-analysis/task2/
# print sorted result
# sort 2itemsets_50.txt | uniq | sort -nr



# support value = 100
hadoop fs -rm -r /yt8m-analysis/task2/2itemsets_100_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/2itemsets_mapper.py,hdfs:///yt8m-analysis/task2/2itemsets_reducer.py \
-mapper 'python3 2itemsets_mapper.py' \
-reducer 'python3 2itemsets_reducer.py 100' \
-input /preprocessed_data/category.txt \
-output /yt8m-analysis/task2/2itemsets_100_output

# save result
hadoop fs -text /yt8m-analysis/task2/2itemsets_100_output/* > ./2itemsets_100.txt
hadoop fs -put ./2itemsets_100.txt /yt8m-analysis/task2/
# print sorted result
# sort 2itemsets_100.txt | uniq | sort -nr

