import csv
import os, sys

# Edit the variable 'path' to the proper folder you want to edit files
path = r"C:\Users\"
files = os.listdir(path)
# i = 0

for file in enumerate(files):
    # Edit the path to the proper CSV you want to access
    with open(r"D:\Maker\quotes.csv",'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in csvreader:
            #str = str(index) + '.png'
            name = row[0]# + '.png'
            new = row[1]# + '.png'

            if os.path.exists(path):
                #os.rename(path, new)
                os.rename(os.path.join(path, name),os.path.join(path, new))

            else:
                print (name + "does not exist")
