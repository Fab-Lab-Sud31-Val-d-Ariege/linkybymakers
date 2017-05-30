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
import time

def chksum(data) :
    """ return checksum as a byte.
    Typical, data = line[:-2]"""
    ck = (sum(bytearray(data.encode("ascii"))) & 0x3F) + 0x20
    return ck


def validDate (ll, prog) :
    """Sometime, when the power fall, incomplete date are written followed
    by a complete one. This routine check this and try to keep the valid date.
    prog = re.compile('^2.*(2[0-9]{3}-.*)') is externally compiled to speed up
    process.
    Warning : this RE leads to a year 3000 bug.
    """
    mat = prog.match(ll)
    if (mat) :
        ll = mat.group(1)

    # check if the date is valid
    # 2017-05-25 15:01:40.703244
    try :
        tt = time.strptime(ll, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError :
        ll = None

    return(ll)

def processFrame (frame, fields) :
    """Transform a frame into 2 lists, one of tags and the other of values.
    If the second argument is an empty list, store all fields. Else only
    the fields whose name is in this argument"""
    csvline = list()
    csvheader = list()

    select = False
    if (len(fields) != 0) : select = True

    for chunk in frame :
        toks = chunk.split()
        if (len(toks) == 1 ) : return(list(), csvheader)

        # sometimes the checksum is a space and is remove by the line stripping
        if (len(toks) == 2 ) : toks.append(" ")

        # check the sum
        if (len(toks[2]) > 1 ) : return(list(), csvheader)
        ck = chksum(toks[0]+' '+toks[1])
        # print(">{0}< >{1}< >{2}<".format(chunk, str(ck.to_bytes(1, "big"), "ascii"), toks[2]))
        if ( ord(toks[2]) != ck ) : return(list(), csvheader)

        # check the field
        if (select and not (toks[0] in fields) ) : continue
        csvline.append(toks[1].lstrip('0'))
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
if (len(sys.argv) < 2) :
    print("usage : frames2csv file.dat [field field ...]")
    print("Exemple : frames2csv data/head.dat PTEC HCHC HCHP TENSION PAPP")
    print("Nota : fields will be stored in the same order as they appears in the frames")
    sys.exit()

# reading loop
fn = sys.argv[1]
ind = open(fn, mode="r")

nfields = 0
if (len(sys.argv) > 2) :
    fields = sys.argv[2:]
    nfields = len(fields)
    print("{0} fields to keep : {1}".format(nfields, fields))
else :
    fields = list()

# output file name
pre, ext = os.path.splitext(fn)
ofn = pre + ".csv"
print(ofn)
oud = open(ofn, mode="w")

# match start of frame
prog = re.compile('^2.*')
# match double date
prog2 = re.compile('^2.*(2[0-9]{3}-.*)')

count = 0
frame = list()

date = ""
csvheader = list()
csvline = list()

# go to next start of frame
for line in ind :
    ll = line.strip()
    if ( prog.match(ll)) :
        date = validDate(ll, prog2)
        if (date == None) : continue
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
        csvline, csvheader = processFrame (frame, fields)
        if (len(csvline) != 0 and len(csvline) == nfields and date != None) :
            if (count == 0) : print("ord,date," + ",".join(csvheader), file=oud)
            print("{0},{1},{2}".format(count, date, ",".join(csvline)), file=oud)

        # clear for next step
        frame.clear()
        date = validDate(ll, prog2)
        if (date == None) : continue
        if (len(csvline) != 0 and len(csvline) == nfields) :
            count +=1

# process last frame
csvline, csvheader = processFrame (frame, fields)
print("{0},{1},{2}".format(count, date, ",".join(csvline)), file=oud)
print("{0} frames found".format(count+1))

# /MAIN ===========================
#********
