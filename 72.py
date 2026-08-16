#Tryng some questios based on tuples and tuple methods
#Create a tuple coordinates = (10, 20) and print both elements.
coordinates= (10,20)
print(coordinates[0])
print(coordinates[1])

#Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple
coordinates_list = list(coordinates)
coordinates_list[0] = 50
coordinates = tuple(coordinates_list)

print(coordinates)