# Name     : Gradescope Converter
# Author   : Ryan Carr
# Modified : 04/15/2019
# Purppose : Converts an existing student roster csv built for Akindi into
# a format compatible with Gradescope. Fake emails are generated using
# first.last@example.com

gradescope = []

# Process existing roster data and convert to gradescope compatible
with open('roster.csv') as fh:
    for line in fh:
        if line.startswith('Section'):
            continue
        lst = line.rstrip().split(',')                # Strip Newline, split on commas
        email = lst[2] + '.' + lst[3] + "@example.com"# First.Last@example.com 
        name = lst[2] + ',' + lst[3]                  # First Last Name
        gradescope.append([name , email, lst[1]])     # Add user to list: Name, Email, ID

# Write gradescope roster to a csv
with open('gradescope.csv', 'w') as fh:
    fh.write('First Name,Last Name,Email,Student ID\n')               # Write header to file
    for user in gradescope:
        fh.write(user[0] + ',' + user[1] + ',' + user[2] + '\n')

print('Output placed in gradescope.csv')
