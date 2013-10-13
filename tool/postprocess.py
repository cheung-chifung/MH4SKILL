#!/usr/bin/python

from os import listdir

RAW_DATA_PATH = "../raw_data"
DATA_PATH = "../data"

csvs = [i for i in listdir(RAW_DATA_PATH) if i.endswith(".csv")]

for csv in csvs:
    sourceFileName = "%s/%s" % (RAW_DATA_PATH, csv)
    targetFileName = "%s/UTF8_%s.txt" % (DATA_PATH, csv)
    source = open(sourceFileName, "rb")
    target = open(targetFileName, "wb")
    target.write(unicode(source.read(), "sjis").encode("utf-8"))
