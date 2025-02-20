cars = ["Audi", "Bmw", "MG", "MS", "Honda"]

# it sorts the list in ascending order
cars.sort(reverse=True)
# print(cars)

bikes = ["Hero", "Honda"]

# adds item to end of the list
# cars.append("Hundai")
# cars.append(bikes)

# adds single single items to the list
cars.extend(bikes)

# for bike in bikes:
#     cars.append(bike)

# adds item to list on specific index
# if index is not in sequence it adds value after last index
cars.insert(30, "ABC")
# print(cars[7])

# pop it removes item from any index (default last)

# print(cars)
# removes last
# removed = cars.pop()
# print(removed)

# removes item at index 1
# removed = cars.pop(2)
# print(removed)

# remove delets item of specific value (removes only 1 instance at a time)
# if item not exits it throws an error
# cars.remove("Honda")

# cars.clear()
# print(cars)

# creates a shallow copy of a list
new_cars = cars.copy()
print(cars)
print(new_cars)

# count method returns the number of times a value appears in the list
print(cars.count("ford"))

# if(cars.count("Honda")>0):
#     print("car exists")
# else:
#     print("car does not exists")

print(cars.index("Honda"))

temp = ["Audi", "Bmw", "MG", ["MS", "Honda", ["Ford", "Toyota"]]]
#         0       1      2        3           

print(temp[3][2].index("Toyota"))

cars.reverse()

print(cars)


sub = [
        ['m1', 'm2','m3','m4'], 
        ['b1', 'b2', 'b3', 'b4']
    ]
sub[0].reverse()
sub[1].reverse()
sub.reverse()

print(sub)

temp2 = ["Audi", "Bmw", "MG", "MS", "Honda"]
#         0       1      2        3       4
#         -5     -4     -3       -2      -1

print(temp2[2:5])
print(temp2[1:])
print(temp2[:3])

print(temp2[-1])
print(temp2[-5:])
