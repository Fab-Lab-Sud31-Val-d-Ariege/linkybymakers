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
#   200
# MODIFICATION HISTORY
#
# NOTES
#
#******
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

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
# def Reader(arg) :
#********

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
fn = "data/frames_2017-05-23.csv"
df = pd.read_csv(fn, sep=",", comment="#")
df["date"] = pd.to_datetime(df.date)

with PdfPages(fn + '.pdf') as pdf:
    for ff in df.columns[2:] :
        plt.figure(figsize=(30, 5))
        plt.title(ff)
        plt.plot(df.date, df[ff], color='blue', linestyle='-')
        # plt.savefig("profilW" + testnb + ".png", bbox_inches='tight')
        pdf.savefig()
        plt.show()

# /MAIN ===========================
#********
