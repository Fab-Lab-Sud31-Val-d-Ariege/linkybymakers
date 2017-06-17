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
# 01iIlLoO
#
#******
# import serial
from datetime import datetime as dt

def chksum(data) :
    """ return checksum as a byte.
    Typical, data = line[:-2]"""
    ck = (sum(bytearray(data.encode("ascii"))) & 0x3F) + 0x20
    return ck

def processLine (line) :
    """Transform a line into 3 fields, tag, data, checksum."""

    toks = line.split()
    if (len(toks) == 1 ) : return(list())

    # sometimes the checksum is a space and is remove by the line stripping
    if (len(toks) == 2 ) : toks.append(" ")

    # check the sum
    if (len(toks[2]) > 1 ) : toks[2] = toks[2][0]

    data = toks[0] + ' ' + toks[1]
    ck = chksum(data)
    print(">{0}< >{1}< >{2}<".format(data, str(ck.to_bytes(1, "big"), "ascii"), toks[2]))
    if ( ord(toks[2]) != ck ) : return(list())

    return(toks[0:2])

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
# serial port for reading data
#ins = serial.Serial(port="/dev/ttyAMA0", baudrate=1200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

# open file from simulator
ins = open("data/simulateur.dat", "rb")

# Datation
start = dt.today()

# create output file name
fn = "frames_" + start.strftime("%Y-%m-%d") + ".dat"
print(fn)
oud = open(fn, mode='ab')

# main loop
for ll in ins :
    # got one line
    if ( len(ll) < 9 ) : continue
    # print(">{0}<".format(ll))
    # check field and checksum, if decoding in error, ignore line
    try :
        ll = ll.decode("ascii").strip()
    except UnicodeDecodeError :
        continue
    print(">{0}<".format(ll))
    toks = processLine(ll)
    print(toks)
    # store in dictionnary


    ## check date change
    #if (now.day != start.day) :
        #start = dt.today()
        #oud.close()
        #fn = "frames_" + start.strftime("%Y-%m-%d") + ".dat"
        #print(fn)
        #oud = open(fn, mode='ab')

# /MAIN ===========================
#********
