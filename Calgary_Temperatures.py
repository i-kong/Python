# =========================================================
# File            : Calgary_Temperatures.py
# Author          : Irene Kong
# Contact Info    : ihykong@gmail.com
# Purpose         : Assignment m05 to find the coldest hour in Calgary for Sep 2019.
# Dependencies    : None yet
# =========================================================

import csv as c
import math as m

# =========================================================
# Constants and defaults
# =========================================================

FIELD_YEAR = 5
FIELD_MONTH = 6
FIELD_DAY = 7
FIELD_HOUR = 8
FIELD_TEMP = 9

currentColdestTemp = 100
currentColdestHour = ['Not set yet']

# =========================================================
# Prompts user to enter year, month, and date.
# Splits the user's entry by the commas and assigns them to variables.
# =========================================================

userDataStr = input('Enter the year, month, and day. Ex. 2019,9,30: ').split(',')
userYear = int(userDataStr[0])
userMonth = int(userDataStr[1])
userDay = int(userDataStr[2])

# =========================================================
# Opens and set up csv file for reading.
# Skips first line of headers.
# For each row in the csv file, stores relevant data into variables.
# Then uses if statement to identify row with the year,month,day that matches user input.
# Then checks to see if the row's temperature is lower than current coldest temperature.
# If the row's temperature is lower than the current coldest temperature, saves the hour and temperature to the global variables.
# Outputs message of the coldest hour and temperature on the given day.
# =========================================================

with open('2019_09_calgary_hourly.csv', 'r') as inputFile:
    csvFile = c.reader(inputFile, dialect='excel')
    next(csvFile)
    for row in csvFile:
        fileYear = int(row[FIELD_YEAR])
        fileMonth = int(row[FIELD_MONTH])
        fileDay = int(row[FIELD_DAY])
        fileHour = row[FIELD_HOUR]
        fileTemp = float(row[FIELD_TEMP])
        if fileYear == userYear and fileMonth == userMonth and fileDay == userDay:
            if fileTemp < currentColdestTemp:
                currentColdestHour = fileHour
                currentColdestTemp = currentTemp
print(f'The coldest hour on {userYear}-{userMonth}-{userDay} is {currentColdestHour} at {currentColdestTemp} degrees C.\n')
print("Done ...")
