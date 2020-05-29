# First block: User inputs desired continent and sees total cases for three countries in that continent

from statistics import mean

continents = {"Africa": {"Nigeria":8344, "Ghana":6964, "South Africa":24268},
             "Europe": {"Uk":265227, "Russia":370680, "France":182722},
             "North America": {"USA":1733961, "Canada":86939, "Mexico":74560},
             "Asia":{"China":82994, "India":164761, "Turkey":158762},
             "South America":{"Brazil":396654, "Argentina":13228, "Columbia":23003}}

continent = input("Enter the continent of your choice: ")

if continent in continents.keys():
    for item,value in continents[continent].items():
        print(item, value)
    print("The mininmum value is ", min(continents[continent].values()))
    print("The maximum value is ", max(continents[continent].values()))
    print("The sum is ", sum(continents[continent].values()))          
    print("The mean value is ", mean(continents[continent].values()))   
                 
        
             

#Second block: After user sees cases in selected continent, program asks if user wants more details

continent_details = {"Africa": {"Total cases":84123, "Active cases":45647, "Recovered cases":35788, "Total deaths":2287},
               "Europe": {"Total cases":1944334, "Active cases":847955, "Recovered cases":926548, "Total deaths":170061},
               "North America": {"Total cases":1953386, "Active cases":1221849, "Recovered cases":600758, "Total deaths":118405},
                "Asia": {"Total cases":1044072, "Active cases":393020, "Recovered cases":601859, "Total deaths":29017},
                 "South America": {"Total cases":697644, "Active cases":381531, "Recovered cases":275131,"Total deaths":34138}    
               }

response = input("Do you want more details? [yes/no] ")

if response == "yes":
    for item,value in continent_details[continent].items():
        print(item, value)
        
elif response == "no":
    print("Thank you")
    
else:
    print("Invalid response")
# This program contains data for 5 continents with 3 countries for each.          
