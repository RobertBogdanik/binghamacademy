##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/19/2023                   #
# Filename: 12.2.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################


class Location:
    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getMaxValue(self):
        return self.maxValue

def locateLargest(a):
    row = 0
    column = 0
    maxValue = a[0][0]

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > maxValue:
                maxValue = a[i][j]
                row = i
                column = j

    return Location(row, column, maxValue)


rows = eval(input("Enter the number of rows: "))
columns = eval(input("Enter the number of columns: "))

a = []
for i in range(rows):
    row = input(f"Enter row {i}: ")
    a.append([eval(x) for x in row.split()[0:columns]])

location = locateLargest(a)

print(f"The location of the largest element is {location.getMaxValue()} at ({location.getRow()}, {location.getColumn()})")
