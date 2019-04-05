# Name     : Roster Generator
# Author   : Ryan Carr
# Modified : 04/05/2019
# Purppose : Build a CSV file with pseudo-random names and IDs associated with
# the students. This is purely for testing purposes.

from random import choice

FIRST_NAMES = ["James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles","Christopher","Daniel","Matthew","Anthony","Donald","Mark","Paul","Steven","Andrew","Kenneth","George","Joshua","Kevin","Brian","Edward","Mary","Patricia","Jennifer","Linda","Elizabeth","Barbara","Susan","Jessica","Sarah","Margaret","Karen","Nancy","Lisa","Betty","Dorothy","Sandra","Ashley","Kimberly","Donna","Emily","Carol","Michelle","Amanda","Melissa","Deborah"]
LAST_NAMES = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson","Garcia","Martinez","Robinson","Clark","Rodriguez","Lewis","Lee","Walker"]

ID_START             = 11111111 # ID number to start at
SECTION_START        = 1        # Section number to start with
STUDENT_COUNT        = 100      # Total number of students to generate
STUDENTS_PER_SECTION = 25       # Number of students per section

temp_roster = set()
roster = set()

count = 0

while len(temp_roster) < STUDENT_COUNT:
    temp_roster.add(choice(FIRST_NAMES) + "," + choice(LAST_NAMES))

for name in temp_roster:
    if count == 25:
        SECTION_START += 1
        count = 0
    else:
        count += 1
        
    roster.add(str(SECTION_START) + "," + str(ID_START) + "," + name)
    ID_START += 1

with open("roster.csv", "w") as fh:
    fh.write("Section,Student ID,First Name,Last Name\n")
    for name in roster:
        fh.write(name + "\n")

print("Done! File saved as roster.csv")
