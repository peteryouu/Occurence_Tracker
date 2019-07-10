import csv
import matplotlib as plt
import numpy
from sklearn import linear_model


x = input('File name:')


occurence = {}

def file_open(file_name):
    with open(file_name,'r') as fh:
        dates = csv.DictReader(fh)
        for row in dates:
            if row['Dates'] not in occurence:
                occurence[row['Dates']] = 1
            else:
                occurence[row['Dates']] += 1


file_open(x)


o_keys = list(occurence.keys())
o_values = list(occurence.values())
