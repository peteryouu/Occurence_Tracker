import csv
x = input('File name:')
occurence = {}
with open(x,'r') as fh:
    dates = csv.DictReader(fh)
    for row in dates:
        if row['Dates'] not in occurence:
            occurence[row['Dates']] = 1
        else:
            occurence[row['Dates']] += 1

    print(occurence)
