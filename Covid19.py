#Incomplete task, couldn't finish
#Problem:
#I was not able to get the code to output the min, max, mean and sum of countries, it only outputs the particular cotinent details when the user selects.        


continents = {"Africa": {"Nigeria":8344, "Ghana":6964, "South Africa":24268},
             "Europe": {"Uk":265227, "Russia":370680, "France":182722},
             "North America": {"USA":1733961, "Canada":86939, "Mexico":74560},
             "Asia":{"China":82994, "India":164761, "Turkey":158762},
             "South America":{"Brazil":396654, "Argentina":13228, "Columbia":23003}}

continent = input("Enter the continent of your choice: ")

if continent in continents.keys():
    for item,value in continents[continent].items():
        print(item, value)
             

#After user sees cases in selected continent, program asks if user wants more details

continent_details = {"Africa": {"Total cases":84123, "Active cases":45647, "Recovered cases":35788, "Total deaths":2287},
               "Europe": {"Total cases":1944334, "Active cases":847955, "Recovered cases":926548, "Total deaths":170061},
               "North America": {"Total cases":1953386, "Active cases":1221849, "Recovered cases":600758, "Total deaths":118405},
               }
continents = input("Do you want to more details?, Enter the continent name ")

continent_info = continent_details.get(continents, None)

# continent_info would be:

if continent_info:
    print(f'\nContinent is:{continents }')
    print(f'Total cases: {continent_info["Total cases"]}')
    print(f'Active cases: {continent_info["Active cases"]}')
    print(f'Recovered cases: {continent_info["Recovered cases"]}')
    print(f'Total deaths: {continent_info["Total deaths"]}\n')
 else:
     print("Stop")
