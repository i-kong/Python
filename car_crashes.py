# =============================================================================
# File            : car_crashes.py
# Author          : Irene Kong
# Contact Info    : ihykong@gmail.com
# Purpose         : Lab 05 part 1 - Process car crash data and outputs the total number of crashes within specified tolerance and creates a list of those crashes.
# Dependencies    : None yet
# =============================================================================

import csv as c
import math as m

# =============================================================================
# Constants and defaults
# =============================================================================
inFileName = 'crashes.csv'

prjExt = '_geo.prj'
csvExt = '_geo.csv'
csvtExt = '_geo.csvt'

FIELD_LAT = 0
FIELD_LONG = 2
FIELD_CRASH = 3

USER_LAT = 0
USER_LONG = 1
USER_TOLERANCE = 2

id = 1
totalCrashes = 0

# =============================================================================
# Determines the position of the period.
# Saves text from the position of the period and all characters afterwards into variable inExt.
# Replaces text matching inExt from the input file's name with other text specified in another variable.
# =============================================================================
whereIsTheDot = inFileName.index('.')

inExt = inFileName[whereIsTheDot:]

prjFileName = inFileName.replace(inExt, prjExt)
geoCSVFileName = inFileName.replace(inExt, csvExt)
typesFileName = inFileName.replace(inExt, csvtExt)

# =============================================================================
# Creates files/opens prjFileName and typesFileName for writing data into them.
# Writes data into the two files.
# =============================================================================
with open(prjFileName, 'w') as prjFile , open(typesFileName, 'w') as typesFile:
    prjFile.write(f'EPSG:4326')
    typesFile.write(f'Integer,Integer,WKT')

# =============================================================================
# Prompts user for latitude, longitude, and tolerance.
# Extract data from user input to place into variables.
# =============================================================================
userDataStr = input('Enter a latitude, longitude and a tolerance. E.g. 49.25,-123.00,0.05: ').split(',')

userLat = float(userDataStr[USER_LAT])
userLong = float(userDataStr[USER_LONG])
userTolerance = float(userDataStr[USER_TOLERANCE])

# =============================================================================
# Open crashes.csv for reading and create output file for writing.
# Create csv reader.
# Skip row of headers in csvFile.
# Write headers on geoCSVFile then starts new line.
# For each row in csvFile, calculates the distance from row coordinates to user entered coordinates.
# If the distance is within tolerance, it write data to a new row on geoCSVFile.
# =============================================================================
with open('crashes.csv', 'r') as datafile, open(geoCSVFileName, 'w') as geoCSVFile:
    csvFile = c.reader(datafile, dialect='excel')
    next(csvFile)
    geoCSVFile.write(f'id,crashes,geom\n')
    for record in csvFile:
        crashLat = float(record[FIELD_LAT])
        crashLong = float(record[FIELD_LONG])
        distDiffLat = crashLat - userLat
        distDiffLong = crashLong - userLong
        distance = m.sqrt(distDiffLat**2+distDiffLong**2)
        if distance < userTolerance:
            crashes = int(record[FIELD_CRASH])
            totalCrashes += crashes
            id += 1
            geoCSVFile.write(f'{id},{crashes},"POINT({crashLong} {crashLat})"\n')

# =============================================================================
# Output message for total crashes within tolerance of the coordinates entered by the user.
# =============================================================================
print(f'The total number of crashes is : {totalCrashes}\n')
print("Done ...")
