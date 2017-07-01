#!/usr/bin/make
# Edit this file to define constants and custom build targets.
# target for making everything

.PHONY: all
all : convert draw store

%.csv: %.dat
	python3 frames2csv.py $^ PTEC HCHC HCHP TENSION PAPP

%.pdf: %.csv
	python3 la-data.py $^

.PHONY : convert
convert :
	for ii in data/*.dat; do \
		python3 frames2csv.py $$ii PTEC HCHC HCHP TENSION PAPP; \
	done

.PHONY : draw
draw :
	for ii in data/*.csv; do \
		python3 la-data.py $$ii ; \
	done

.PHONY : store
store:
	mv *.dat DAT/
	mv *.pdf PDF/
