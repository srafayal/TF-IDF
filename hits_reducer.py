#!/usr/bin/env python
# hits_reducer.py
# Syed Rafayal
# A reducer program for creating word,filename,count file for next steps
import sys

current_key = None
current_count = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into word, file_name, count by tab
    word, file_name, count = line.strip().split('\t')
    # generate key by word, file_name
    key = '%s\t%s' % (word, file_name)
    # check current key with previous key and increase count
    if current_key == None:
        current_key = key
        current_count = eval(count)
    elif current_key == key:
        current_count += eval(count)
    else:
        print "%s\t%s" % (current_key, current_count)
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # next Mapper step, i.e. the input for tf_mapper.py
        # tab-delimited;
        current_key = key
        current_count = eval(count)
# output the last if needed!
print "%s\t%s" % (current_key, current_count)
