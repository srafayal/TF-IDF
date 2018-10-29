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

