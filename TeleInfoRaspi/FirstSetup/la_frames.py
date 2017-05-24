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
#   2017-05-13
# MODIFICATION HISTORY
#
# NOTES
#
#******
import sys
import serial

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

instream = serial.Serial(port="/dev/ttyAMA0", baudrate=1200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

while True :
    cc = instream.read(1)
    #print("> {0} <".format(cc))
    if cc == b'\x02' :
        sys.stdout.write("\n====== STX")
    elif cc == b'\x03' :
        sys.stdout.write("\n====== ETX")
    else :
        sys.stdout.write(cc.decode("ascii"))

# /MAIN ===========================
#********
