secoundsinyear = 60*60*24*365
birth = secoundsinyear//7
death = secoundsinyear//13
immigrant = secoundsinyear//45

population = 312032486

for year in range(6):
    population += birth + immigrant - death
    print(f"Year {year}: {population}")