##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

#Converts from feet to meters
def footToMeter(foot):
    return 0.305 * foot


# Converts from meters to feet
def meterToFoot(meter):
    return meter / 0.305

print("Feet\tMeters\t|\tMeters\tFeet")

feet = 1
meter = 20

for x in range(10):
    print(f"{feet}\t\t{footToMeter(feet)}\t|\t{meter}\t\t{meterToFoot(meter)}")
    feet += 1
    meter += 6
