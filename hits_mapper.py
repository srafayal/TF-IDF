#!/usr/bin/env python
# hits_mapper.py
# Syed Rafayal
# A mapper program for creating word,filename,fixed value 1

import sys
import os
# read file path
file_path = os.environ["map_input_file"]
# get file name from file path variable
file_name = os.path.split(file_path)[-1]  # get the names

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for hits_reducer.py
        #
        # tab-delimited;
        # the trivial word count is 1
        print "%s\t%s\t1" % (word, file_name)
