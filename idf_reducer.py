#!/usr/bin/env python
# idf_reducer.py
# Syed Rafayal
# A reducer program for calculating TF by counting number for file_name, word

from math import log10, sqrt
import sys

# declare and assign global variable
current_word = None
current_count = None
keys = []
doc_no = 124

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    # split the line into word, file_name, tf, count by tab
    word, file_name, tf, count = line.strip().split()
    # make key by word, file_name, tf
    key = "%s\t%s\t%s" % (word, file_name, tf)
    # compare with new word with previous word
    # if none then assign  current_word ,current_count and add key into list
    # if match then add current count with present count and add key into list
    # if not match then calculate IDF for all key and print into STDOUT
    # output : word, file_name, tf, idf
    if word == None:
        current_word = word
        current_count = eval(count)
        keys.append(key)
    elif current_word == word:
        current_count += eval(count)
        keys.append(key)
    else:
        for item in keys:
            idf = log10(float(doc_no) / float(current_count))
            print "%s\t%s" % (item, str(idf))
        current_word = word
        current_count = eval(count)
        keys = [key]

# calculate IDF for all rest of the key and print into STDOUT
# output : word, file_name, tf, idf
for key in keys:
    idf = log10(float(doc_no) / float(current_count))
    print "%s\t%s" % (item, str(idf))
