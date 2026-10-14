#define a list of cities
cities = ["Málaga", "Cádiz", "Sevilla", "Huelva", "Córdoba", "Jaén", "Granada", "Almería"]

#2d city in the list
print(cities[1])

#the last city
print(cities[-1])

#between the 5th and 6th city
print(cities[4:6])

#create a new list from the cities list
andaluciaOriental = cities[-3:]
print (andaluciaOriental)

#ask if a city exist in cities list
cityName = input("Write a city:").strip().upper()
#if cityName in cities:
#    print(cityName,"exists")
#else:
#    print(cityName,"Doesn't exists")

#check if the cityName exist in cities list
#case insensitive
#tip1:loop the list cities
#tip2: check in each loop upper = upper
#tip3: use a boolean variable to know if has find it
exist = False

for city in cities:
    if cityName == city.upper():
        exist = True
        break

if exist:        
    print ("Exist!!")
else: 
    print ("NOOOO Exist!!")


