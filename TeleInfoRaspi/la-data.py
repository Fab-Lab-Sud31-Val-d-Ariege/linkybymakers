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
import sys
import os
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
# MAIN ============================
if (len(sys.argv) < 2) :
    print("usage : la-data file.csv True/False")
    print("True/False to show or not the PAPP curves,")
    print("Always store the pdf.")
    print("Exemple : la-data data/frames_2017-05-23.csv")
    sys.exit()

# reading loop
ifn = sys.argv[1]
df = pd.read_csv(ifn, comment="#")
df["date"] = pd.to_datetime(df.date)
df.set_index("date", inplace=True, verify_integrity=True)
# transform levels in numbers
df.loc[df.PTEC=="HP..","PTEC"] = 1
df.loc[df.PTEC=="HC..","PTEC"] = 0

# in no arguments, show = True
show = True
if (len(sys.argv) == 3) :
    if (sys.argv[2] != "True") :
        show = False

ofn = os.path.splitext(ifn)[0] + ".pdf"
with PdfPages(ofn) as pdf :
    for ff in df.columns[1:] :
        plt.figure(figsize=(30, 5))
        plt.title(ff)
        # plt.plot(df.date, df[ff], color='blue', linestyle='-')
        df[ff].plot()
        # plt.savefig("mlgqlm.png", bbox_inches='tight')
        pdf.savefig()
        print("drawing {0}".format(ff))
        if ( show and (ff == "PAPP") ) :
            plt.show()
        else :
            plt.close()

# /MAIN ===========================
#********
