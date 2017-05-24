#! /usr/bin/env python3
# coding: utf8
# $Id$
#
#****h* main_module/module [1.0] *
# NAME
#       tool -- explanation
# COPYRIGHT
#   Copyright (c) 2007--today by Francis Micheli.
#   Gnu Public Licence
#   See the file "license.terms" for information on usage and
#   distribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
# FUNCTION
#
# AUTHOR
#   Francis Micheli
# CREATION DATE
#   2017-05-14
# MODIFICATION HISTORY
#
# NOTES
# Keep only useful fields
# Check number of fields as well as checksum
# Bad checksum became NA
# Select while reading ?
# Store as CSV
#
#******
import sys
import os
import re
# from lib_frames import *

def processFrame (frame) :
    """Transform a frame into 2 lists, one of tags and the other of values"""
    csvline = list()
    csvheader = list()

    for chunk in frame :
        toks = chunk.split()
        if (len(toks) == 1 ) : return(list(), list())
        # sometimes the checksum is a space and is remove by the line stripping
        if (len(toks) == 2 ) : toks.append(" ")
        csvline.append(toks[1])
        csvheader.append(toks[0])

    return(csvline, csvheader)

#****f* module/procname [1.0] *
# NAME
#
# FUNCTION
#
# INPUTS
#
# RESULT
#
# SOURCE
#
# MAIN ============================
# reading loop
fn = sys.argv[1]
ind = open(fn, mode="r")

# output file name
pre, ext = os.path.splitext(fn)
ofn = pre + ".csv"
print(ofn)
oud = open(ofn, mode="w")

# match start of frame
prog = re.compile('^20.*')

count = 0
frame = list()

date = ""
csvheader = list()
csvline = list()

# go to next start of frame
for line in ind :
    ll = line.strip()
    if ( prog.match(ll)) :
        date = ll
        break

# start again after first date
for line in ind :
    # error, sometimes the checksum is a space...
    ll = line.strip()
    if ( not prog.match(ll)) :
        # not a frame start, should be a frame line
        frame.append(ll)
    else :
        # found start of a frame
        # process preceding frame unless it is empty
        if (len(frame) == 0) : continue
        csvline, csvheader = processFrame (frame)
        if (len(csvline) != 0 ) :
            if (count == 0) : print("ord,date," + ",".join(csvheader), file=oud)
            print("{0},{1},{2}".format(count, date, ",".join(csvline)), file=oud)

        # clear for next step
        frame.clear()
        date = ll
        count +=1

# process last frame
csvline, csvheader = processFrame (frame)
print("{0},{1},{2}".format(count, date, ",".join(csvline)), file=oud)
print("{0} frames found".format(count+1))

# /MAIN ===========================
#********
