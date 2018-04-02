#Setup
docker-compose up -d
docker attach hadoop
cd $HADOOP_PREFIX

#Copying files in
bin/hadoop fs -copyFromLocal /datadrop/purchases.txt.gz
bin/hadoop fs -ls

#Running map reduce and viewing and copying output
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.1.jar grep input output 'dfs[a-z.]+'
bin/hadoop fs -getmerge words /results/example

#Running streaming Task
bin/hadoop \
    jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar  \
    -mapper /codedrop/purchasesMap.py \
    -reducer /codedrop/purchasesReduce.py \
    -input purchases.txt.gz \
    -output purchasesByStore

bin/hadoop fs -cat purchasesByStore/* 

bin/hadoop \
    jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar  \
    -mapper /codedrop/paymentCountMap.py \
    -reducer /codedrop/paymentCountReduce.py \
    -input purchases.txt.gz \
    -output paymentByType

bin/hadoop fs -cat paymentByType/* 

Extra or alternate commands
1. Copy ouptut as folder: bin/hadoop fs -copyToLocal words /results  
2. Use a diffrent prefix for hdfs: bin/hfds dfs == bin/hadoop df (first is more modern)
3. Delete folder in hdfs: bin/hadoop fs -rm -r -skipTrash datadrop
4. view output of hdfs folder: bin/hadoop fs -cat words/* 
