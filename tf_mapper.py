#!/usr/bin/env python
# tf_mapper.py
# Syed Rafayal
# A mapper program for collecting all data as one format from STDIN and
# just print all to other format for reducer

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into word, filename, count
    word, filename, count = line.strip().split('\t')
    print "%s\t%s\t%s" % (filename, word, count)
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for tf_reducer.py
    #
    # tab-delimited;
