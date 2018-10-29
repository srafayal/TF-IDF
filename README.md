# TF-IDF
 Compute TFIDF scores for all words in all documents  and build an inverted index
Introduction

Here in this study, the whole work is divided into two parts. In the first part, I'll represent a simple MapReduce implementation for compute TF-IDF and then in the second part the information retrieval is implemented by using TF-IDF scores. 

For calculating TF-IDF scores from scratch, I have followed total 4 steps. In this 4 steps, I have used 4 mappers and 3 reducers; and all steps are implemented by Python.
Last mapper will generate finest TF-IDF scores files with all information (word, file name, TF, IDF and TF-IDF scores) and this file will be used as a second step’s input.
Python code has also been used in the second part and ‘spark-submit’ has been used for executing python code. The command ‘spark-submit’ transfers two additional arguments for query and return top ‘N’ matching documents.




Dataset

Here, I am using the specific dataset provided for this study which is bbcsport.zip. The dataset contains different folders for different article like athletics, cricket, football, rugby, tennis. I choose dataset for article cricket for this experiment. The folder contains 124 files.

At the beginning, before implementing the Hadoop MapReduce, the dataset is uploaded to HDFS .
The Virtualbox folder is :/root/lab/
High level Architecture diagram

The high level architecture diagram of this system is as follows:


Fig 2: Architecture diagram of the System

Data Flow Diagram

The system data flow diagram is shown as follows:



Fig 3: Data Flow DIagram of the System
PART 1

In first part, I have used MapReduce for compute TF-IDF. I used it because I have controlled all the input-output of the system and implemented all the steps of calculation from scratch to get the result of TF-IDF score. I have used python for creating mapper and reducer files and have used hadoop-streaming for executing all python files. 

Here, ‘hadoop-streaming’ version is necessary for executing code.

find /usr -name *hadoop-streaming*


For calculating TF-IDF scores from scratch, I have followed total 4 steps. Below all necessary steps are described.


Step 1 (Hits): 

Here, mapper (hits_mapper.py) takes files from HDFS and starts reading line by line and split all the lines by word. Mapper generates output with three columns related data where the columns are word, filename and 1. This output is used for reducer as input. 

Reducer will take that informations by using STDIN and will start counting by using keys named word and Filename and generate output file with Word, Filename and count column and stores into HDFS.

Input Folder: (HDFS)/user/root/exam/files/*.txt
Output Folder: (HDFS)/user/root/exam/output/tf_out

Commands:

hadoop jar /usr/hdp/2.5.0.0-1245/hadoop-mapreduce/hadoop-streaming-2.7.3.2.5.0.0-1245.jar \
-file /root/lab/hits_mapper.py -mapper hits_mapper.py \
-file /root/lab/hits_reducer.py -reducer hits_reducer.py \
-input /user/root/exam/files/*.txt  \
-output /user/root/exam/output/hits_out

Step 2 (Generate Term Frequency (TF)):

Mapper will take input file from HDFS which was created by previous step and will read all the line and split it into word, filename, count. It will print filename, word, count as string by using Python STDOUT for next reducer.

Reducer will split all coming line into filename, word, count and will store all into a list. It will also store total number of words of individual file into a dictionary. After that the list will be used for loop for calculating word’s TF by using below formula and print word, file_name,tf. System will be generated output file for next step.

 

Input Folder: (HDFS)/user/root/exam/output/hits_out/part-00000
Output Folder: (HDFS)/user/root/exam/output/tf_out
Commands:
hadoop jar /usr/hdp/2.5.0.0-1245/hadoop-mapreduce/hadoop-streaming-2.7.3.2.5.0.0-1245.jar \
-file /root/lab/tf_mapper.py -mapper tf_mapper.py \
-file /root/lab/tf_reducer.py -reducer tf_reducer.py \
-input /user/root/exam/output/hits_out/part-00000 \
-output /user/root/exam/output/tf_out



Steps 3 (Inverse Document Frequency (IDF)): 

Mapper will take input file from HDFS which was created by previous step and will read all the line and add “1” into each line. New line will be print as string by using Python STDOUT for next reducer.

Reducer will split all coming line into word, file_name, tf, count and will generate key by using word, file_name, tf. Reducer will check all the word with previous word and if match then calculate total count and store the key into list. If match not found, then it will calculate individual word IDF for key’s list. After calculating, it will print word, file_name, tf, idf as output. System will generate output file for next step.
 
Input Folder: (HDFS)/user/root/exam/output/tf_out/part-00000
Output Folder: (HDFS)/user/root/exam/output/idf_out


Commands:

hadoop jar /usr/hdp/2.5.0.0-1245/hadoop-mapreduce/hadoop-streaming-2.7.3.2.5.0.0-1245.jar \
-file /root/lab/idf_mapper.py -mapper idf_mapper.py \
-file /root/lab/idf_reducer.py -reducer idf_reducer.py \
-input /user/root/exam/output/tf_out/part-00000 \
-output /user/root/exam/output/idf_out

Step4 
(Term Frequency–Inverse Document Frequency (TF-IDF)):

Mapper will take input file from HDFS which was created by previous step and will read all the line and calculate TF-IDF and will print as string by using Python STDOUT for next part for retrieving top N matching documents.





We do not need any reducer because of mapper is sufficient for calculating .




Input File: (HDFS)/user/root/exam/output/idf_out/part-00000
Output Files: (HDFS)/user/root/exam/output/tf_idf_out/part-00000
                           /user/root/exam/output/tf_idf_out/part-00001




Commands:

hadoop jar /usr/hdp/2.5.0.0-1245/hadoop-mapreduce/hadoop-streaming-2.7.3.2.5.0.0-1245.jar \
-numReduceTasks 0 \
-file /root/lab/tf_idf_mapper.py -mapper tf_idf_mapper.py \
-input /user/root/exam/output/idf_out/part-00000 \
-output /user/root/exam/output/tf_idf_out










Sample output:



Codes:








PART 2

Text Document Retrieval

In this section,the top N matching documents list is retrieved by using TF-IDF scores which are previously calculated in part 1. The output file of previous part is taking as an input of this section for processing. Query (one or more words) and the top N value are transferring as argument to the system.



Implementation: 

Here, I have used ‘Python’ for coding and ‘spark-submit’ for executing code file to hadoop. By the ‘spark-submit’ command I have send two additional argument, one is query (one or more words) and the other is a value N and it will make the search  system near-real time. This facility is giving me flexibility to coding this search system.

After getting argument values, the number of argument and type will be checked. If it is valid then SparkConf, SparkContext and call main method will be initialized. Main method implements the necessary equation for getting list of top matching documents.

Input Files(HDFS):
/user/root/exam/output/tf_idf_out/part-0000*


Sample Commands:

spark-submit  --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m /root/lab/query.py 'Zimbabwe bowlers endure hard toil' 1







Code:



Results

Experiment:
I took 2 query and change N’s value 3 times for each query.

Experiment 1:
Query: ‘Brendon McCullum’

Top N: 1

Result: 


Top N: 3

Result: 


Top N: 5

Result: 


Experiment 2:
Query: ‘Zimbabwe bowlers endure hard toil’

Top N: 1

Result: 


Top N: 3

Result: 


Top N: 5

Result: 




Conclusion

To utilize MapReduce is very useful when working with bigdata. When working with large data, MapReduce is a method that allows to map the data using a particular attribute or grouping and then the reducer reduce that using transformation or aggregation process. I used Hadoop because Hadoop has the most popular libraries for MapReduce to work with large data and it uses cluster computing for fast processing of large data. In this experiment also Python libraries are used. I found Python easiest and most simple to set up with this task. It seems Python contains the most clear library for MapReduce. Also Spark is used to quickly running the data as well as mapping and reducing. All these tools make the system near real time.

