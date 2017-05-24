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
import serial
from datetime import datetime as dt

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
ins = serial.Serial(port="/dev/ttyAMA0", baudrate=1200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

# wait until a frame start
while ins.read(1) != b'\x02' :
    continue

# reading loop
start = dt.today()
# create file name
fn = "frames_" + start.strftime("%Y-%m-%d") + ".dat"
print(fn)
oud = open(fn, mode='ab')

# main loop
buff = bytearray()
now = dt.today()
while (True) :
    cc = ins.read(1)
    # new start of frame
    if (cc == b'\x02') :
        now = dt.today()
    # end of frame, print data
    elif (cc == b'\x03') :
        oud.write("{0}".format(now).encode())
        oud.write(buff)
        buff.clear()
    # just store the byte in the buffer
    else :
        buff += cc
    # check date change
    if (now.day != start.day) :
        start = dt.today()
        oud.close()
        fn = "frames_" + start.strftime("%Y-%m-%d") + ".dat"
        print(fn)
        oud = open(fn, mode='ab')

# /MAIN ===========================
#********
