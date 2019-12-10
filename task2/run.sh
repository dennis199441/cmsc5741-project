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



'''
hadoop fs -rm -r /yt8m-analysis/task2/3itemsets_step1_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/3itemsets_step1_mapper.py,hdfs:///yt8m-analysis/task2/3itemsets_step1_reducer.py \
-mapper 'python3 3itemsets_step1_mapper.py' \
-reducer 'python3 3itemsets_step1_reducer.py' \
-input /yt8m-analysis/task2/2itemsets.txt \
-output /yt8m-analysis/task2/3itemsets_step1_output

hadoop fs -text /yt8m-analysis/task2/3itemsets_step1_output/* > ./3itemsets_step1.txt
hadoop fs -put ./3itemsets_step1.txt /yt8m-analysis/task2/





hadoop fs -rm -r /yt8m-analysis/task2/3itemsets_step2_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/3itemsets_step2_mapper.py,hdfs:///yt8m-analysis/task2/3itemsets_step2_reducer.py \
-mapper 'python3 3itemsets_step2_mapper.py' \
-reducer 'python3 3itemsets_step2_reducer.py' \
-input /yt8m-analysis/task2/2itemsets.txt \
-output /yt8m-analysis/task2/3itemsets_step2_output

hadoop fs -text /yt8m-analysis/task2/3itemsets_step2_output/* > ./3itemsets_step2.txt
hadoop fs -put ./3itemsets_step2.txt /yt8m-analysis/task2/





hadoop fs -rm -r /yt8m-analysis/task2/3itemsets_step3_output/

yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-files hdfs:///yt8m-analysis/task2/3itemsets_step3_mapper.py,hdfs:///yt8m-analysis/task2/3itemsets_step3_reducer.py \
-mapper 'python3 3itemsets_step3_mapper.py' \
-reducer 'python3 3itemsets_step3_reducer.py' \
-input /preprocessed_data/category.txt \
-output /yt8m-analysis/task2/3itemsets_step3_output

hadoop fs -text /yt8m-analysis/task2/3itemsets_step3_output/*

'''