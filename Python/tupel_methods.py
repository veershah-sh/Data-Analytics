students = ("raghav", "jay", "dev", "pooja", "jinal", "jay")

print(type(students))

print(students.count("jay"))

print(students.index("dev"))

print(len(students))

# how to mutate tuple

# 1. create a list from tuple
new_students = list(students)
print(type(new_students))

# 2. add item / remove item from list
new_students.append("abc")
print(new_students)

# 3. convert list to tuple
students = tuple(new_students)
print(students)