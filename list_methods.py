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
print(cars[7])

# pop it removes item from any index (default last)

print(cars)
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
print(cars)


