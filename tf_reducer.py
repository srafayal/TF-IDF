#!/usr/bin/env python
# tf_reducer.py
# Syed Rafayal
# A reducer program for calculating TF by counting number for file_name, word
import sys

# declare and assign global variable
current_word = None
prev_filename = None
current_count = 0
word = None
N = 0
filename_count = {}
lines = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # adding line in the list
    lines.append(line)
    # split the line into file_name, word, count by tab
    file_name, word, count = line.split('\t')
    # convert count (currently a string) to int
    count = int(count)
    # check previous file name with current file name
    # if same then add count with N
    # otherwise change previous file name and reset N value by 0
    # and update dictionary 'filename_count' by previous filename
    if prev_filename == file_name:
        N = N + count
    else:
       if prev_filename != None:
           filename_count[prev_filename] = N
       N = 0
       prev_filename = file_name
# update last value
filename_count[prev_filename] = N

# read all the line from list
for line in lines:
    # split the line into file_name, word, count by tab
    file_name, word, count = line.split('\t')
    for name in filename_count:
        if file_name == name:
            # calculate Term Frequency
            tf = float(count)/float(filename_count[name])
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # next Mapper step, i.e. the input for idf_mapper.py
            # tab-delimited;
            print "%s\t%s\t%s" % (word, file_name, str(tf))
