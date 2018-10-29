#!/usr/bin/env python
# idf_mapper.py
# Syed Rafayal
# A mapper program for collecting all data as one format from STDIN and
# just print all to same format with 1 for reducer

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    print "%s\t1" % line.strip()
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for idf_reducer.py
    #
    # tab-delimited;
