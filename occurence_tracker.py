import csv
import matplotlib.pyplot as pyplot
import numpy
from sklearn import linear_model


x = input('File name:')


occurence = {}

def file_open(file_name):
    with open(file_name,'r') as fh:
        dates = csv.DictReader(fh)
        for row in dates:
            if row['Dates'] == "":
                pass
            if row['Dates'] not in occurence:
                occurence[row['Dates']] = 1
            else:
                occurence[row['Dates']] += 1


file_open(x)


o_keys = list(occurence.keys())
o_keys_count = []
for i in range(1,len(o_keys)+1):
    o_keys_count.append(i)
o_values = list(occurence.values())

def bestfit(x,y):
    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)
    n = len(x)

    top = sum([xi*yi for xi,yi in zip(x,y)]) - n*x_avg * y_avg
    bot = sum([xi**2 for xi in x]) - n*x_avg**2

    b = top/bot
    a = y_avg - b*x_avg

    return a,b

def fix1Darray(a_ray):
    return numpy.array(a_ray).reshape(-1,1)

o_keys_count = fix1Darray(o_keys_count)
o_values = fix1Darray(o_values)

def plotter():
    regr = linear_model.LinearRegression()
    regr.fit(o_keys_count,o_values)
    a,b = bestfit(o_keys_count,o_values)
    pyplot.plot(o_keys[::30],o_values[::30])
    yfit = [a+b * xi for xi in o_keys_count]
    pyplot.plot(o_keys_count[::30],yfit[::30])
    pyplot.xticks(ticks = [1,7,14,21,28,33])
    pyplot.xlabel('date')
    pyplot.ylabel('frequency of submissions')
    pyplot.show()

plotter()


#pyplot.plot(o_keys[::30],o_values[::30])

