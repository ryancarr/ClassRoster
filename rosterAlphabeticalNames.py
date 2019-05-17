# Name    : Name Alphabetizer
# Author  : Ryan Carr
# Created : 04/23/2019
# Purpose : Process the rosters generated for Akindi and Gradescope and
# create an alphabetical list of all students into a small csv file.

names = []

with open('gradescope.csv', 'r') as fh:
    for line in fh:
        if line.startswith("First"): continue
        contents = line.split(',')
        names.append(contents[0] + ' ' + contents[1])

names.sort()

with open('names.csv', 'w') as fh:
    for name in names:
        fh.write(name + '\n')

print('Names successfully alphabetized.')
