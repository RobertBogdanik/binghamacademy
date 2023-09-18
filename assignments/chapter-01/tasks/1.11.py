##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 08/??/2023                   #
# Filename: 1.11.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

secoundsinyear = 60*60*24*365
birth = secoundsinyear//7
death = secoundsinyear//13
immigrant = secoundsinyear//45

population = 312032486

for year in range(6):
    population += birth + immigrant - death
    print(f"Year {year}: {population}")