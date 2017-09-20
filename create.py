import csv

with open('persons.csv', 'wb') as csvfile:
    #filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter = csv.writer(csvfile, delimiter=',',  escapechar=',', quoting=csv.QUOTE_NONE)
    filewriter.writerow(['id', 'diagnosticList', 'ecuList', 'model', 'moduleId', 'DunspartNumtraceIdsn', 'vin', 'name'])

    for i in range(0, 2000):
        filewriter.writerow(['Car-DK0' + str(i+10000), '8453372', '8453372', 'DF91', 'DK0' + str(i+10000), 'DK' + str(i+100000), str(i + 12345678901231000), 'DF91-' + str(i)])