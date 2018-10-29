#!/usr/bin/env python
# tf_idf_mapper.py
# Syed Rafayal
# A mapper program for collecting all data from STDIN and
# calculate tf-idf

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into word, file_name, tf, idf
    word, file_name, tf, idf = line.split('\t')
    # calculate tf-idf
    tfidf = float(tf)*float(idf)
    print '%s\t%s\t%s\t%s\t%s' % (word, file_name, tf, idf, str(tfidf))
    # write the results to STDOUT (standard output);
    # tab-delimited;